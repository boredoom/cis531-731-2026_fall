"""contracts.py - Deal contracts for CIS 531 MP 5 (CorpusChunk Pipeline)."""
from dataclasses import dataclass
from datetime import datetime
import deal

APPROVED_SOURCES = frozenset({"genius", "spotify", "musicbrainz", "rym"})
APPROVED_LICENSES = frozenset(
    {"fair_use", "public_domain", "cc_by_sa", "all_rights_reserved_educational"}
)
MAX_CHUNK_DURATION_SEC = 30.0

@dataclass(frozen=True)
class CorpusChunk:
    record_id: str
    track: str
    source_id: str
    ts_start: datetime
    ts_end: datetime
    text: str
    ingest_ts: datetime
    license_class: str

@deal.pre(lambda chunk: chunk.ts_start < chunk.ts_end, message="Temporal monotonicity violation")
@deal.pre(lambda chunk: 0.0 < (chunk.ts_end - chunk.ts_start).total_seconds() <= MAX_CHUNK_DURATION_SEC, message="BoundedChunking violation")
@deal.pre(lambda chunk: chunk.source_id.strip().lower() in APPROVED_SOURCES, message="Whitelist gate violation")
@deal.pre(lambda chunk: chunk.license_class.strip().lower() in APPROVED_LICENSES, message="Provenance gate violation")
@deal.pre(lambda chunk: bool(chunk.record_id and chunk.record_id.strip()), message="Empty record_id violation")
@deal.pre(lambda chunk: bool(chunk.track and chunk.track.strip()), message="Empty track violation")
@deal.pre(lambda chunk: bool(chunk.text and chunk.text.strip()), message="Empty text violation")
@deal.pre(lambda chunk: chunk.ingest_ts >= chunk.ts_end, message="Causality violation")
def validate_chunk(chunk: CorpusChunk) -> bool:
    return True

def check_record(record_id, track, source_id, ts_start, ts_end, text, ingest_ts, license_class) -> bool:
    try:
        c = CorpusChunk(record_id, track, source_id, ts_start, ts_end, text, ingest_ts, license_class)
        return validate_chunk(c)
    except (deal.PreContractError, TypeError, AttributeError, ValueError):
        return False

if __name__ == "__main__":
    t0 = datetime(2026, 10, 20, 12, 0, 0)
    t1 = datetime(2026, 10, 20, 12, 0, 20)
    t2 = datetime(2026, 10, 20, 12, 0, 25)
    assert check_record("r1", "track1", "genius", t0, t1, "lyric words", t2, "fair_use") is True
    assert check_record("r2", "track1", "unapproved", t0, t1, "words", t2, "fair_use") is False
    print("Deal contracts validated successfully.")
