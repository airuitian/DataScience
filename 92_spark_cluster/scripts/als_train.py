import os
import sys
spark_home = os.environ.get('SPARK_HOME', None)
sys.path.insert(0, os.path.join(spark_home, 'python'))
sys.path.insert(0, os.path.join(spark_home, 'python/lib/py4j-0.10.7-src.zip'))

os.environ["PYSPARK_PYTHON"]="/home/ec2-user/anaconda3/bin/python"

from pyspark.sql import SparkSession

from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row


def getSparkSession(master, app_name):
    spark = SparkSession.builder.master(master)\
                                .appName(app_name)\
                                .getOrCreate()

    return spark

def load_train_test(session, data_path):

    lines = session.read.text(data_path).rdd
    parts = lines.map(lambda row: row.value.split("\t"))
    ratingsRDD = parts.map(lambda p: Row(userId=int(p[0]), movieId=int(p[1]),
                                         rating=float(p[2]), timestamp=int(p[3])))
    global ratings
    ratings = session.createDataFrame(ratingsRDD)
    (train_set, test_set) = ratings.randomSplit([0.8, 0.2])

    return train_set, test_set


def SaveModel(session):
    """存储模型"""
    try:
        model.save(session, Path+"ALSmodel")
        print("模型已存储")
    except Exception:
        print("模型已存在,先删除后创建")


def train(train_set, rank, maxIter):
    # Note we set cold start strategy to 'drop' to ensure we don't get NaN evaluation metrics
    global als
    als = ALS(rank=rank, maxIter=maxIter, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating",
              coldStartStrategy="drop")

    global model
    model = als.fit(train_set)

    return als, model

def evaluate(test_set):

    # Evaluate the model by computing the RMSE on the test data
    predictions = model.transform(test_set)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                    predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)

    print("Root-mean-square error = " + str(rmse))

def predict_sample():
    # Generate top 10 movie recommendations for each user
    userRecs = model.recommendForAllUsers(10)
    # Generate top 10 user recommendations for each movie
    movieRecs = model.recommendForAllItems(10)

    # 给指定用户推荐10部电影
    users = ratings.select(als.getUserCol()).distinct().limit(3)
    userSubsetRecs = model.recommendForUserSubset(users, 10)
    # 选择最喜欢指定电影的10个用户
    movies = ratings.select(als.getItemCol()).distinct().limit(3)
    movieSubSetRecs = model.recommendForItemSubset(movies, 10)
    # $example off$
    userRecs.show()
    movieRecs.show()
    userSubsetRecs.show()
    movieSubSetRecs.show()


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Parameters's number is wrong.")
        sys.exit(1)

    master = sys.argv[1]
    app_name = sys.argv[2]
    data_path = sys.argv[3]
    rank = int(sys.argv[4])
    maxIter = int(sys.argv[5])
    print(maxIter)
    session = getSparkSession(master, app_name)
    print("Loading rating data")
    train_set, test_set = load_train_test(session, data_path)
    print("ALS Traning")
    train(train_set, rank, maxIter)
    print("Evaluate training error")
    evaluate(train_set)
    #predictions = model.transform(test)
    #evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
    #                                predictionCol="prediction")
    #rmse = evaluator.evaluate(predictions)

    predict_sample()
    session.stop()
