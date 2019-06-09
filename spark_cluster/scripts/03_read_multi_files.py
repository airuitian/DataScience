import numpy as np

from pyspark.sql import SparkSession

spark = SparkSession.builder.master('spark://172.31.45.49:7077')\
                           .appName('Save and Load Files')\
                           .getOrCreate()

# Read files under a folder
sales_rdd = spark.sparkContext.wholeTextFiles('../data/sales/')

def convert_record_to_value(x):
    sum_sales = []
#'iphone,8000\niwhach,4000\nipad,3000\nipad,3000\n')
    for items in x.strip().split('\n'):
        product, price = items.split(',')
        sum_sales.append(float(price))

    return np.average(sum_sales) 
 
sales_rdd = sales_rdd.mapValues(convert_record_to_value)
#sales_rdd = sales_rdd.flatMap(lambda x: x[1].strip().split(','))
print(sales_rdd.collect())
