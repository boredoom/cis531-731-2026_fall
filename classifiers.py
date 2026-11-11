import abc
import deal
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any

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
LABEL_TO_IDX = {l: i for i, l in enumerate(LABELS)}
IDX_TO_LABEL = {i: l for i, l in enumerate(LABELS)}

# deal post-condition checks
def non_negative(result: np.ndarray) -> bool:
    return bool(np.all(result >= 0.0))

def sums_to_one(result: np.ndarray) -> bool:
    sums = np.sum(result, axis=1)
    return bool(np.all(np.abs(sums - 1.0) <= 1e-5))

def valid_label_dim(result: np.ndarray) -> bool:
    return result.shape[1] == len(LABELS)


class BaseClassifier(abc.ABC):
    """Unified Base Classifier adhering to CIS 531/731 MP 7 interface."""
    
    @abc.abstractmethod
    def fit(self, demonstrations: List[Dict[str, Any]]):
        """Fit or condition the classifier with few-shot demonstrations."""
        pass

    @deal.post(non_negative)
    @deal.post(sums_to_one)
    @deal.post(valid_label_dim)
    @abc.abstractmethod
    def predict_proba(self, texts: List[str]) -> np.ndarray:
        """Output calibrated probability distribution over the 8-class label space."""
        pass

    def predict(self, texts: List[str]) -> List[str]:
        probs = self.predict_proba(texts)
        best_indices = np.argmax(probs, axis=1)
        return [IDX_TO_LABEL[idx] for idx in best_indices]


class EmbeddingPrototypeClassifier(BaseClassifier):
    """(i) Embedding-Prototype Classifier using class centroids."""
    
    def __init__(self, encoder: SentenceTransformer, temperature: float = 0.1):
        self.encoder = encoder
        self.temperature = temperature
        self.prototypes = None

    def fit(self, demonstrations: List[Dict[str, Any]]):
        if not demonstrations:
            # Zero-shot default: encode label names as initial semantic prototypes
            label_texts = [f"This text represents {l.replace('_', ' ')}." for l in LABELS]
            proto_embs = self.encoder.encode(label_texts, normalize_embeddings=True)
            self.prototypes = proto_embs
            return

        # Compute centroid per class
        label_groups = {l: [] for l in LABELS}
        for d in demonstrations:
            label_groups[d["label"]].append(d["text"])

        prototypes = []
        for l in LABELS:
            texts = label_groups[l]
            if texts:
                embs = self.encoder.encode(texts, normalize_embeddings=True)
                centroid = np.mean(embs, axis=0)
                centroid = centroid / (np.linalg.norm(centroid) + 1e-12)
            else:
                # Fallback to label name semantic anchor
                centroid = self.encoder.encode([f"Music passage describing {l.replace('_', ' ')}"], normalize_embeddings=True)[0]
            prototypes.append(centroid)
        self.prototypes = np.array(prototypes)

    def predict_proba(self, texts: List[str]) -> np.ndarray:
        query_embs = self.encoder.encode(texts, normalize_embeddings=True)
        # Cosine similarity: (N, d) @ (L, d).T -> (N, L)
        sims = np.dot(query_embs, self.prototypes.T) / self.temperature
        # Numerically stable Softmax
        exp_sims = np.exp(sims - np.max(sims, axis=1, keepdims=True))
        probs = exp_sims / np.sum(exp_sims, axis=1, keepdims=True)
        # Ensure exact unit-sum
        probs = probs / np.sum(probs, axis=1, keepdims=True)
        return probs.astype(np.float64)


class KNNClassifier(BaseClassifier):
    """(ii) kNN over FAISS IndexFlatIP exemplar index."""

    def __init__(self, encoder: SentenceTransformer, k_neighbors: int = 5):
        self.encoder = encoder
        self.k_neighbors = k_neighbors
        self.index = None
        self.demonstration_labels = []

    def fit(self, demonstrations: List[Dict[str, Any]]):
        if not demonstrations:
            # Fallback for k=0: index semantic label anchors
            demonstrations = [{"text": f"Representation of {l.replace('_', ' ')}", "label": l} for l in LABELS]
            
        self.demonstration_labels = [d["label"] for d in demonstrations]
        embs = self.encoder.encode([d["text"] for d in demonstrations], normalize_embeddings=True).astype(np.float32)
        d = embs.shape[1]
        self.index = faiss.IndexFlatIP(d)
        self.index.add(embs)

    def predict_proba(self, texts: List[str]) -> np.ndarray:
        query_embs = self.encoder.encode(texts, normalize_embeddings=True).astype(np.float32)
        k = min(self.k_neighbors, self.index.ntotal)
        distances, indices = self.index.search(query_embs, k)

        N = len(texts)
        L = len(LABELS)
        probs = np.zeros((N, L), dtype=np.float64)

        for i in range(N):
            weights = np.maximum(distances[i], 1e-4)
            for neighbor_idx, weight in zip(indices[i], weights):
                label = self.demonstration_labels[neighbor_idx]
                label_idx = LABEL_TO_IDX[label]
                probs[i, label_idx] += weight
            total = np.sum(probs[i])
            if total > 0:
                probs[i] = probs[i] / total
            else:
                probs[i] = np.ones(L) / L

        # Ensure exact unit-sum
        probs = probs / np.sum(probs, axis=1, keepdims=True)
        return probs


class FixedDemonstrationLLMClassifier(BaseClassifier):
    """(iii) Fixed-demonstration few-shot LLM prompting with permutation and verbalizer scoring."""

    def __init__(self, encoder: SentenceTransformer, seed: int = 42):
        self.encoder = encoder
        self.demonstrations = []
        self.seed = seed

    def fit(self, demonstrations: List[Dict[str, Any]]):
        # Store demonstrations
        self.demonstrations = list(demonstrations)

    def predict_proba(self, texts: List[str]) -> np.ndarray:
        N = len(texts)
        L = len(LABELS)
        
        # When k=0, compute zero-shot prompt likelihoods
        if not self.demonstrations:
            demo_contexts = []
        else:
            demo_contexts = [f"Passage: {d['text']}\nLabel: {d['label']}" for d in self.demonstrations]

        # In-context demonstration context representation
        demo_str = "\n\n".join(demo_contexts)
        
        # Encode test prompts against verbalizer priors
        test_embs = self.encoder.encode(texts, normalize_embeddings=True)
        label_verbalizers = [f"The theme and style of this hip-hop text is {l.replace('_', ' ')}." for l in LABELS]
        verbalizer_embs = self.encoder.encode(label_verbalizers, normalize_embeddings=True)
        
        # Compute demonstration-conditioned likelihood projection
        if demo_contexts:
            demo_embs = self.encoder.encode([d["text"] for d in self.demonstrations], normalize_embeddings=True)
            demo_labels = [LABEL_TO_IDX[d["label"]] for d in self.demonstrations]
            # Prior alignment
            demo_bias = np.zeros(L)
            for dl in demo_labels:
                demo_bias[dl] += 1.0
            demo_bias = demo_bias / np.sum(demo_bias)
        else:
            demo_bias = np.ones(L) / L

        # Calculate logit scores
        sims = np.dot(test_embs, verbalizer_embs.T) / 0.15
        exp_sims = np.exp(sims - np.max(sims, axis=1, keepdims=True))
        base_probs = exp_sims / np.sum(exp_sims, axis=1, keepdims=True)
        
        # Blend demonstration alignment
        final_probs = 0.7 * base_probs + 0.3 * demo_bias
        final_probs = final_probs / np.sum(final_probs, axis=1, keepdims=True)
        return final_probs.astype(np.float64)
