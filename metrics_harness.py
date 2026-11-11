import json
import numpy as np
from sklearn.metrics import f1_score, precision_recall_fscore_support
from typing import Dict, Any, List

LABELS = [
    "Hustle_Narrative",
    "Regional_Authenticity",
    "Lyrical_Sovereignty",
    "Systemic_Critique",
    "Boom_Bap",
    "G_Funk",
    "Trap",
    "Chopper"
]

def bootstrap_macro_f1(y_true: List[str], y_pred: List[str], n_bootstraps: int = 1000, seed: int = 42) -> Dict[str, float]:
    """Calculate 95% non-parametric bootstrap confidence intervals for Macro-F1."""
    rng = np.random.RandomState(seed)
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    n = len(y_true)
    
    bootstrap_f1s = []
    for _ in range(n_bootstraps):
        boot_idx = rng.choice(n, size=n, replace=True)
        f1 = f1_score(y_true[boot_idx], y_pred[boot_idx], labels=LABELS, average="macro", zero_division=0)
        bootstrap_f1s.append(f1)
        
    bootstrap_f1s = np.array(bootstrap_f1s)
    ci_lower = float(np.percentile(bootstrap_f1s, 2.5))
    ci_upper = float(np.percentile(bootstrap_f1s, 97.5))
    point_est = float(f1_score(y_true, y_pred, labels=LABELS, average="macro", zero_division=0))
    
    return {
        "macro_f1": point_est,
        "ci_95_lower": ci_lower,
        "ci_95_upper": ci_upper
    }

def compute_graded_metric(predictions_path: str, eval_path: str = "eval_mp7.jsonl") -> Dict[str, Any]:
    """INV-12: Official Graded Metric Evaluation Harness."""
    with open(eval_path, "r") as f:
        ground_truth = {json.loads(line)["id"]: json.loads(line)["label"] for line in f}
        
    with open(predictions_path, "r") as f:
        preds = [json.loads(line) for line in f]
        
    y_true = []
    y_pred = []
    for p in preds:
        item_id = p["id"]
        if item_id in ground_truth:
            y_true.append(ground_truth[item_id])
            y_pred.append(p["predicted_label"])
            
    stats = bootstrap_macro_f1(y_true, y_pred)
    p_class, r_class, f_class, _ = precision_recall_fscore_support(y_true, y_pred, labels=LABELS, zero_division=0)
    
    per_class = {}
    for idx, label in enumerate(LABELS):
        per_class[label] = {
            "precision": float(p_class[idx]),
            "recall": float(r_class[idx]),
            "f1": float(f_class[idx])
        }
        
    return {
        "grading_eligible": True,
        "evaluation_source": eval_path,
        "macro_f1": stats["macro_f1"],
        "ci_95_lower": stats["ci_95_lower"],
        "ci_95_upper": stats["ci_95_upper"],
        "per_class": per_class
    }

def compute_dev_metric(predictions_path: str, eval_path: str) -> Dict[str, Any]:
    """Advisory metrics for internal validation splits (grading_eligible=False)."""
    res = compute_graded_metric(predictions_path, eval_path)
    res["grading_eligible"] = False
    return res
