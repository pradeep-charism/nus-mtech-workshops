from pyspark import SparkConf, SparkContext

conf = SparkConf().setAppName("Create RDD")
conf = conf.setMaster("local[*]")
spark = SparkContext(conf=conf)
spark.setLogLevel("ERROR")
# in Python from a local collection
myCollection = "Spark RDD is for any text, structured or unstructured - Big Data Processing".split(" ")
words = spark.parallelize(myCollection, 2)
print(words.collect())

# in Python from a File or a directory
myFileLineCount = spark.textFile("data/dummy.txt").count()
print(myFileLineCount)

myFileWordCount = spark.textFile("data/dummy.txt").flatMap(lambda line: line.split(" ")).count()
print(myFileWordCount)

myFileCount = spark.wholeTextFiles("data").count()
print(myFileCount)
