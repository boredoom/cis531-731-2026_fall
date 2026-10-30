"""
contracts.py: Operational contract validation for document admittance and vector database upsert.
Implements deal contracts enforcing schema invariants: EmbeddingCompleteness and NoOrphanEmbeddings.
"""

from __future__ import annotations
import math
from typing import Any, Dict, List, Set
import deal

# Permitted licenses under academic fair use guidelines
AUTHORIZED_LICENSES: Set[str] = {
    "academic_research",
    "fair_use_evaluation",
    "creative_commons",
    "public_domain",
}

VALID_SECTIONS: Set[str] = {
    "intro", "verse", "chorus", "hook", "bridge", "outro", "freestyle"
}

EXPECTED_EMBEDDING_DIM: int = 768


# ============================================================================
# CONTRACT SPECIFICATIONS: ADMIT_DOCUMENT
# ============================================================================

@deal.pre(
    lambda doc: isinstance(doc, dict)
    and "document_id" in doc
    and "license_class" in doc
    and "raw_lyrics" in doc
    and "region" in doc
    and doc["license_class"] in AUTHORIZED_LICENSES,
    message="Precondition Failed: Document lacks valid license_class or required metadata."
)
@deal.pre(
    lambda doc: isinstance(doc.get("raw_lyrics"), str) and len(doc["raw_lyrics"].strip()) >= 50,
    message="Precondition Failed: raw_lyrics payload is too brief or invalid type."
)
@deal.post(
    lambda result: isinstance(result, dict)
    and result.get("admitted") is True
    and "lineage_hash" in result
    and result.get("document_id") is not None,
    message="Postcondition Failed: Admitted document lacks verified lineage registration."
)
def admit_document(doc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Evaluates an incoming Bronze document record against licensing, payload,
    and provenance criteria, returning a verified Silver admission ticket.
    """
    import hashlib

    # Compute a deterministic lineage hash over document metadata and text
    hasher = hashlib.sha256()
    hasher.update(doc["document_id"].encode("utf-8"))
    hasher.update(doc["license_class"].encode("utf-8"))
    hasher.update(doc["raw_lyrics"].encode("utf-8"))
    lineage_hash = hasher.hexdigest()

    return {
        "admitted": True,
        "document_id": doc["document_id"],
        "license_class": doc["license_class"],
        "region": doc["region"],
        "lineage_hash": lineage_hash,
        "char_count": len(doc["raw_lyrics"]),
    }


# ============================================================================
# INVARIANTS: EMBEDDING COMPLETENESS & NO ORPHAN EMBEDDINGS
# ============================================================================

def check_embedding_completeness(records: List[Dict[str, Any]]) -> bool:
    """
    Invariant: Asserts that every record contains a valid dense vector of dimension
    EXPECTED_EMBEDDING_DIM, populated exclusively by finite real numbers (no NaNs or Infs),
    and having unit norm within an epsilon tolerance.
    """
    if not records:
        return False

    for rec in records:
        vec = rec.get("dense_embedding")
        if not isinstance(vec, list) or len(vec) != EXPECTED_EMBEDDING_DIM:
            return False

        # Validate finiteness and calculate norm
        norm_sq = 0.0
        for val in vec:
            if not isinstance(val, (int, float)) or math.isnan(val) or math.isinf(val):
                return False
            norm_sq += val * val

        # Allow float precision epsilon around unit sphere (1.0 +/- 1e-3)
        if abs(math.sqrt(norm_sq) - 1.0) > 1e-3:
            return False

    return True


def check_no_orphan_embeddings(records: List[Dict[str, Any]], admitted_doc_ids: Set[str]) -> bool:
    """
    Invariant: Asserts that every vector payload's foreign key (document_id)
    resolves to an admitted, registered document in the parent corpus catalog.
    """
    if not admitted_doc_ids:
        return False

    for rec in records:
        doc_id = rec.get("document_id")
        if not doc_id or doc_id not in admitted_doc_ids:
            return False

    return True


# ============================================================================
# CONTRACT SPECIFICATIONS: VDB_UPSERT
# ============================================================================

@deal.pre(
    lambda records, admitted_doc_ids: isinstance(records, list) and len(records) > 0,
    message="Precondition Failed: Upsert batch must be a non-empty list."
)
@deal.pre(
    lambda records, admitted_doc_ids: check_embedding_completeness(records),
    message="Precondition Failed: Invariant Violation -> EmbeddingCompleteness check failed."
)
@deal.pre(
    lambda records, admitted_doc_ids: check_no_orphan_embeddings(records, admitted_doc_ids),
    message="Precondition Failed: Invariant Violation -> NoOrphanEmbeddings check failed."
)
@deal.post(
    lambda result: result.get("upserted_count", 0) > 0 and result.get("status") == "SUCCESS",
    message="Postcondition Failed: Vector database failed to confirm atomic insertion."
)
def vdb_upsert(records: List[Dict[str, Any]], admitted_doc_ids: Set[str]) -> Dict[str, Any]:
    """
    Executes atomic vector database upsert, guaranteeing complete embeddings
    and parent lineage resolution before persistence.
    """
    # Simulated atomic upsert into vector database index
    upserted_count = len(records)
    return {
        "status": "SUCCESS",
        "upserted_count": upserted_count,
        "index_type": "HNSW",
        "metric": "inner_product",
    }
