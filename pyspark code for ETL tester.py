from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, countDistinct

# Step 1: Start Spark
spark = SparkSession.builder.appName("ETLTestingTemplate").getOrCreate()

# Step 2: Load Source Data (CSV + SQL Example)
source_sales = spark.read.option("header", True).csv("/mnt/raw/sales.csv")
source_customers = spark.read.format("jdbc") \
    .option("url", "jdbc:sqlserver://server:1433;databaseName=RetailDB") \
    .option("dbtable", "dbo.Customers") \
    .option("user", "username") \
    .option("password", "password") \
    .load()

# Step 3: Transform Data
transformed_df = source_sales.join(source_customers, "CustomerID") \
    .filter(col("Amount") > 0) \
    .withColumnRenamed("Amount", "SaleAmount")

# Step 4: Load into Delta Lake
transformed_df.write.format("delta").mode("overwrite").save("/mnt/curated/sales_delta")
target_df = spark.read.format("delta").load("/mnt/curated/sales_delta")

# -------------------------------
# ETL TESTING CHECKLIST
# -------------------------------

# 1. Row Count Validation
assert source_sales.count() == target_df.count(), "Row count mismatch!"

# 2. Schema Validation
print("Source Schema:")
source_sales.printSchema()
print("Target Schema:")
target_df.printSchema()

# 3. Null Checks
null_counts = target_df.select([count(col(c)).alias(c) for c in target_df.columns])
null_counts.show()

# 4. Duplicate Checks
dup_count = target_df.groupBy("CustomerID").count().filter(col("count") > 1).count()
assert dup_count == 0, "Duplicates found!"

# 5. Business Rule Validation (Amount > 0)
invalid_rows = target_df.filter(col("SaleAmount") <= 0).count()
assert invalid_rows == 0, "Invalid SaleAmount values found!"

# 6. Referential Integrity (CustomerID must exist)
missing_customers = target_df.filter(col("CustomerID").isNull()).count()
assert missing_customers == 0, "Missing Customer references!"

# 7. Partition Validation
print(f"Target partitions: {target_df.rdd.getNumPartitions()}")

# 8. Sample Record Comparison
source_sales.filter(col("CustomerID") == 101).show()
target_df.filter(col("CustomerID") == 101).show()
