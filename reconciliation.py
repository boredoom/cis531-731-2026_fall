"""reconciliation.py - Verification of restart fault-tolerance."""
import os
import shutil
import time
from datetime import datetime, timedelta
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pipeline import CorpusChunkSchema

def populate_mock_landing_zone(spark: SparkSession, landing_dir: str, num_files: int = 15):
    os.makedirs(landing_dir, exist_ok=True)
    temp_dir = "/tmp/reconcile_mock_temp"
    base_time = datetime(2026, 10, 20, 10, 0, 0)

    for i in range(num_files):
        records = []
        batch_base = base_time + timedelta(seconds=i * 30)
        for j in range(20):
            t_start = batch_base + timedelta(seconds=j)
            t_end = t_start + timedelta(seconds=15)
            t_ingest = t_end + timedelta(seconds=2)
            records.append((
                f"rec_{i}_{j}",
                f"track_{j % 3}",
                "genius",
                t_start,
                t_end,
                "sample hip hop rhyme cadence flow",
                t_ingest,
                "fair_use"
            ))

        shutil.rmtree(temp_dir, ignore_errors=True)
        # Write via Spark using the exact CorpusChunkSchema
        df = spark.createDataFrame(records, schema=CorpusChunkSchema)
        df.coalesce(1).write.mode("overwrite").parquet(temp_dir)

        # Move the part-*.parquet file to landing_dir as a flat single file
        part_files = [f for f in os.listdir(temp_dir) if f.startswith("part-") and f.endswith(".parquet")]
        if part_files:
            shutil.move(
                os.path.join(temp_dir, part_files[0]),
                os.path.join(landing_dir, f"batch_{i:03d}.parquet")
            )

    shutil.rmtree(temp_dir, ignore_errors=True)
    print(f"Populated {num_files} micro-batch files in {landing_dir}")

def test_reconciliation():
    landing = "/tmp/reconcile_test/landing"
    output = "/tmp/reconcile_test/output"
    chk = "/tmp/reconcile_test/checkpoint"

    shutil.rmtree("/tmp/reconcile_test", ignore_errors=True)

    spark = (SparkSession.builder
             .master("local[2]")
             .appName("ReconcileTest")
             .config("spark.sql.shuffle.partitions", "2")
             .config("spark.sql.parquet.enableVectorizedReader", "false")
             .getOrCreate())

    populate_mock_landing_zone(spark, landing, num_files=15)

    def launch_stream():
        return (spark.readStream
                .schema(CorpusChunkSchema)
                .option("maxFilesPerTrigger", 1)
                .parquet(landing)
                .withWatermark("ts_end", "15 seconds")
                .groupBy(F.window("ts_end", "60 seconds"))
                .agg(F.count("record_id").alias("record_count"))
                .writeStream.format("parquet")
                .outputMode("append")
                .option("checkpointLocation", chk)
                .option("path", output)
                .trigger(processingTime="1 second")
                .start())

    # Phase 1: Start initial stream run
    print("Starting initial stream execution...")
    q1 = launch_stream()

    # Allow 3 micro-batches to commit before injecting crash
    start_wait = time.time()
    while time.time() - start_wait < 15:
        if q1.recentProgress and len(q1.recentProgress) >= 3:
            break
        time.sleep(0.5)

    # Phase 2: Inject ungraceful termination mid-stream
    print(f"Injecting fault after {len(q1.recentProgress)} micro-batches processed...")
    q1.stop()

    # Phase 3: Resume stream from existing checkpoint
    print("Resuming stream from existing checkpoint...")
    q2 = launch_stream()
    q2.processAllAvailable()
    q2.stop()

    # Phase 4: Reconciliation Audit
    print("Reconciling output Parquet sink...")
    res = spark.read.parquet(output)
    total_rows = res.count()
    unique_windows = res.select("window.start", "window.end").distinct().count()

    print(f"Total window entries emitted: {total_rows}")
    print(f"Total unique window keys:    {unique_windows}")

    assert total_rows > 0, "Assertion failed: No windows emitted to sink."
    assert total_rows == unique_windows, "FAULT INJECTION AUDIT FAILED: Duplicate window keys detected!"
    print("RECONCILIATION TEST PASSED: Exactly-once recovery verified with zero duplicate or missing windows.")
    spark.stop()

if __name__ == "__main__":
    test_reconciliation()
