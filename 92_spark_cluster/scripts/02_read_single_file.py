import os
import sys
spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.10.7-src.zip'))

from pyspark.sql import SparkSession

spark = SparkSession.builder.master('spark://172.31.45.49:7077')\
                           .appName('Save and Load Files')\
                           .getOrCreate()

sales_rdd = spark.sparkContext.textFile('../data/sales/sales_1')
print(sales_rdd.collect())


