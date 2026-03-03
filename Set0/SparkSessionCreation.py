from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[2]") \
    .appName("SparkSessionCreation") \
    .getOrCreate()

print("Spark started")

spark.stop()
print("Spark stopped")
