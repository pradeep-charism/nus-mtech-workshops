from pyspark import SparkConf, SparkContext
from io import StringIO

conf = SparkConf().setAppName("Create RDD")
conf = conf.setMaster("local[*]")
spark = SparkContext(conf=conf)
spark.setLogLevel("ERROR")


nasdaqRecords = spark.textFile("assets/NASDAQ_20220216.csv")
print(nasdaqRecords.take(10))