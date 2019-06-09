from pyspark.sql import SparkSession

spark = SparkSession.builder.master('spark://172.31.45.49:7077')\
                           .appName('Save and Load Files')\
                           .getOrCreate()

sales_rdd = spark.sparkContext.textFile('../data/sales/sales_1')
print(sales_rdd.collect())


