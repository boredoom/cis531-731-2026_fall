"""pipeline.py - PySpark Structured Streaming Pipeline for MP 5."""
import sys
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

CorpusChunkSchema = StructType([
    StructField("record_id", StringType(), False),
    StructField("track", StringType(), False),
    StructField("source_id", StringType(), False),
    StructField("ts_start", TimestampType(), False),
    StructField("ts_end", TimestampType(), False),
    StructField("text", StringType(), False),
    StructField("ingest_ts", TimestampType(), False),
    StructField("license_class", StringType(), False),
])

APPROVED_SOURCES = ["genius", "spotify", "musicbrainz", "rym"]
APPROVED_LICENSES = ["fair_use", "public_domain", "cc_by_sa", "all_rights_reserved_educational"]

def run(landing_dir, output_dir, checkpoint_dir):
    spark = (SparkSession.builder
             .appName("CIS531_MP5_CorpusReplay")
             .master("local[2]")
             .config("spark.sql.shuffle.partitions", "2")
             .getOrCreate())

    raw = (spark.readStream
           .schema(CorpusChunkSchema)
           .option("maxFilesPerTrigger", 1)
           .parquet(landing_dir))

    filtered = (raw.filter(F.col("record_id").isNotNull() & (F.length(F.trim("record_id")) > 0))
                   .filter(F.col("track").isNotNull() & (F.length(F.trim("track")) > 0))
                   .filter(F.lower(F.trim("source_id")).isin(APPROVED_SOURCES))
                   .filter(F.lower(F.trim("license_class")).isin(APPROVED_LICENSES))
                   .filter(F.col("ts_start") < F.col("ts_end"))
                   .filter((F.col("ts_end").cast("double") - F.col("ts_start").cast("double")) <= 30.0)
                   .filter(F.col("ingest_ts") >= F.col("ts_end"))
                   .filter(F.col("text").isNotNull() & (F.length(F.trim("text")) > 0)))

    watermarked = filtered.withWatermark("ts_end", "15 seconds")

    tokenized = (watermarked
                 .withColumn("latency_sec", F.col("ingest_ts").cast("double") - F.col("ts_end").cast("double"))
                 .withColumn("tokens", F.split(F.lower(F.regexp_replace("text", r"[^a-zA-Z\s]", "")), r"\s+"))
                 .withColumn("token", F.explode("tokens"))
                 .filter(F.length("token") > 2))

    tumbling = (tokenized.groupBy(F.window("ts_end", "60 seconds"))
                .agg(
                    F.count("record_id").alias("record_count"),
                    F.approx_count_distinct("token", 0.05).alias("approx_distinct_tokens"),
                    F.avg("latency_sec").alias("mean_ingest_latency_sec")
                ))

    q = (tumbling.writeStream.format("parquet")
         .outputMode("append")
         .option("checkpointLocation", checkpoint_dir)
         .option("path", output_dir)
         .trigger(processingTime="10 seconds")
         .start())
    q.awaitTermination()

if __name__ == "__main__":
    landing = sys.argv[1] if len(sys.argv) > 1 else "/tmp/mp5/landing"
    output = sys.argv[2] if len(sys.argv) > 2 else "/tmp/mp5/output"
    chk = sys.argv[3] if len(sys.argv) > 3 else "/tmp/mp5/checkpoint"
    run(landing, output, chk)
