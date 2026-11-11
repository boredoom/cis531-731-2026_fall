import json
import random
import time
import numpy as np
from sentence_transformers import SentenceTransformer
from classifiers import (
    EmbeddingPrototypeClassifier,
    KNNClassifier,
    FixedDemonstrationLLMClassifier,
    LABELS
)
from metrics_harness import compute_graded_metric

SEEDS = [42, 123, 456, 789, 2026]
SHOT_COUNTS = [0, 1, 3, 5, 8]

print("[1/5] Loading shared sentence encoder (cached local all-mpnet-base-v2)...")
encoder = SentenceTransformer("all-mpnet-base-v2")

print("[2/5] Loading evaluation set and candidate exemplars...")
with open("eval_mp7.jsonl", "r") as f:
    eval_set = [json.loads(line) for line in f]

with open("exemplars_pool.jsonl", "r") as f:
    exemplar_pool = [json.loads(line) for line in f]

eval_texts = [item["text"] for item in eval_set]
eval_ids = [item["id"] for item in eval_set]

# Group candidate exemplars by class
exemplars_by_class = {l: [] for l in LABELS}
for item in exemplar_pool:
    exemplars_by_class[item["label"]].append(item)

sweep_results = {
    "Prototype": {k: [] for k in SHOT_COUNTS},
    "kNN": {k: [] for k in SHOT_COUNTS},
    "LLM_FewShot": {k: [] for k in SHOT_COUNTS}
}

all_predictions_log = []
start_time = time.time()

print("[3/5] Executing controlled shot sweep across 5 seeds...")
for k in SHOT_COUNTS:
    for seed in SEEDS:
        rng = random.Random(seed)
        
        # Select k balanced exemplars per class
        demonstrations = []
        if k > 0:
            for l in LABELS:
                available = list(exemplars_by_class[l])
                rng.shuffle(available)
                demonstrations.extend(available[:k])
            # Failure-mode control: Randomize presentation order to eliminate position bias
            rng.shuffle(demonstrations)
            
        models = {
            "Prototype": EmbeddingPrototypeClassifier(encoder),
            "kNN": KNNClassifier(encoder, k_neighbors=max(1, k)),
            "LLM_FewShot": FixedDemonstrationLLMClassifier(encoder, seed=seed)
        }
        
        for name, clf in models.items():
            clf.fit(demonstrations)
            preds = clf.predict(eval_texts)
            probs = clf.predict_proba(eval_texts)
            
            # Log individual predictions
            temp_pred_file = f"/tmp/preds_{name}_k{k}_s{seed}.jsonl"
            with open(temp_pred_file, "w") as pf:
                for idx, (item_id, pred, prob) in enumerate(zip(eval_ids, preds, probs)):
                    record = {
                        "id": item_id,
                        "model": name,
                        "shots_k": k,
                        "seed": seed,
                        "predicted_label": pred,
                        "probabilities": {LABELS[j]: float(prob[j]) for j in range(len(LABELS))}
                    }
                    pf.write(json.dumps(record) + "\n")
                    if seed == 42:
                        all_predictions_log.append(record)
                        
            # Compute INV-12 metric
            metrics = compute_graded_metric(temp_pred_file, "eval_mp7.jsonl")
            sweep_results[name][k].append(metrics["macro_f1"])

print("\n[4/5] Writing master predictions.jsonl...")
with open("predictions.jsonl", "w") as f:
    for rec in all_predictions_log:
        f.write(json.dumps(rec) + "\n")

elapsed = time.time() - start_time
print(f"[OK] Completed sweep in {elapsed:.1f} seconds. Output: predictions.jsonl ({len(all_predictions_log)} records)")

print("\n" + "="*80)
print("                       MP 7 SHOT SWEEP BENCHMARK RESULTS")
print("="*80)
print(f"{'Classifier':<15} | {'k=0 (Macro-F1)':<18} | {'k=1':<10} | {'k=3':<10} | {'k=5':<10} | {'k=8':<10}")
print("-" * 80)

summary_table = {}
for name in ["Prototype", "kNN", "LLM_FewShot"]:
    row_str = f"{name:<15} | "
    summary_table[name] = {}
    for k in SHOT_COUNTS:
        scores = sweep_results[name][k]
        mean_val = np.mean(scores)
        std_val = np.std(scores)
        summary_table[name][k] = {"mean": mean_val, "std": std_val}
        row_str += f"{mean_val:.4f}±{std_val:.3f}   "
    print(row_str)

# Save benchmark summary for report generation
with open("benchmark_summary.json", "w") as f:
    json.dump(summary_table, f, indent=2)

# Compute best configuration per-class metrics
best_metrics = compute_graded_metric("/tmp/preds_Prototype_k8_s42.jsonl", "eval_mp7.jsonl")
with open("best_config_per_class.json", "w") as f:
    json.dump(best_metrics, f, indent=2)
print("[OK] Saved benchmark_summary.json and best_config_per_class.json")
