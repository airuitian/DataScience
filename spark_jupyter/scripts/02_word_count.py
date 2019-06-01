from pyspark import SparkContext

sc = SparkContext( 'local', 'Word Count')
textFile = sc.textFile('../data/words')
word_count = textFile.flatMap(lambda line: line.split(" "))\
                    .map(lambda word: (word,1))\
                    .reduceByKey(lambda a, b : a + b)
word_count.foreach(print)
