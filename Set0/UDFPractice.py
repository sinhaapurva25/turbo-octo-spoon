"""
This script demonstrates the creation of a Spark DataFrame using PySpark.
It performs the following steps:
1. Initializes a Spark session with the application name "SparkUDF" and sets the master to local mode.
2. Defines the schema for the DataFrame with two columns: "Seqno" and "Name".
3. Creates a sample dataset containing two records.
4. Constructs a DataFrame from the sample data and schema.
5. Displays the contents of the DataFrame without truncating the output.
6. Stops the Spark session.
Requirements:
- PySpark must be installed. For Python 3.10.10, it is recommended to use PySpark version 3.3.0 or later.
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkUDF") \
    .master("local[2]") \
    .getOrCreate()

columns = ["Seqno", "Name"]
data = [("1", "Apurva Sinha1"), ("2", "Apurva Sinha2")]


df = spark.createDataFrame(data, columns)
df.show(truncate=False)

spark.stop()
