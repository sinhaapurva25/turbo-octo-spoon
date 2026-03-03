from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import DoubleType, ArrayType
from pyspark.sql.types import StructType, StructField

# ---------------------------------------------------
# 1️⃣ Create Spark Session
# ---------------------------------------------------
sparkConf = SparkConf("spark.master","local[2]", "spark.app.name", "TaxCalculationUDF")
spark = SparkSession.builder \
    .config(sparkConf) \
    .getOrCreate()

# ---------------------------------------------------
# 2️⃣ Sample Schema
# ---------------------------------------------------
schema = StructType([
    StructField("income", DoubleType(), true),
    StructField("deduction", DoubleType(), true),
    StructField("income_components", DoubleType(), true)
    ])

# ---------------------------------------------------
# 3️⃣ Sample Data
# ---------------------------------------------------
data = [
    (100000.0, 10000.0, [50000.0, 30000.0, 20000.0]),
    (75000.0, None, [40000.0, 20000.0]),
    (None, 5000.0, None),
    (120000.0, 20000.0, [60000.0, 40000.0, 20000.0])
 ]

df = spark.createDataFrame(data, schema)

# ---------------------------------------------------
# 4️⃣ Define Normal Python UDF
# ---------------------------------------------------
def calculate_tax(income, deduction, income_components):
    
    # Handle null income
    if income is None:
        income = 0.0
        
    # Handle null deduction
    if deduction is None:
        deduction = 0.0
    
    # If array column is provided, sum it
    if income_components is not None:
        total_income = sum(income_components)
    else:
        total_income = income
    
    taxable_income = total_income - deduction
    
    if taxable_income <= 0:
        return 0.0
    elif taxable_income <= 50000:
        return taxable_income * 0.1
    elif taxable_income <= 100000:
        return taxable_income * 0.2
    else:
        return taxable_income * 0.3

# Register UDF
tax_udf = udf(calculate_tax, DoubleType())

# ---------------------------------------------------
# 5️⃣ Apply UDF
# ---------------------------------------------------
df_with_tax = df.withColumn(
    "tax",
    tax_udf(
        col("income"),
        col("deduction"),
        col("income_components")
    )
)

# ---------------------------------------------------
# 6️⃣ Show Result
# ---------------------------------------------------
df_with_tax.show(truncate=False)

# ---------------------------------------------------
# 7️⃣ Stop Spark Session
# ---------------------------------------------------
spark.stop()