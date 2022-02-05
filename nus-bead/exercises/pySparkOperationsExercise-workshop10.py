# Given the following DataFrame which contains “employee_name”,
# “department”, “country“, “salary”, “age” and “bonus” columns

# Complete the following items:
# a) Create a PySpark DataFrame based on the given RDD.
# b) Show data and print schema
# c) Run groupBy() on “department” columns.
#       Calculate aggregates like minimum, maximum, average, total salary for each group
#       using min(), max(), avg() and sum() aggregate functions respectively.
# d) Run groupBy() on “country” columns.
#       Calculate aggregates like minimum, maximum, average, total salary for each group
#       using min(), max(), avg() and sum() aggregate functions respectively.
from pyspark.sql import SparkSession

data = [("James", "Sales", "SG", 70000, 34, 10000),
        ("Michael", "Sales", "SG", 66000, 56, 20000),
        ("Robert", "Sales", "MY", 61000, 30, 23000),
        ("Maria", "Finance", "MY", 60000, 24, 23000),
        ("Raman", "Finance", "USA", 79000, 40, 24000),
        ("Scott", "Finance", "USA", 63000, 36, 19000),
        ("Jen", "Finance", "UK", 89000, 53, 15000),
        ("Jeff", "Marketing", "UK", 70000, 25, 18000),
        ("Alice", "Marketing", "UK", 78000, 50, 21000),
        ("Ada", "IT", "SG", 83000, 35, 11000),
        ("Jackson", "IT", "MY", 71000, 30, 21000),
        ("Cooper", "IT", "UK", 91000, 40, 21000)]

spark = SparkSession.builder.appName("Pyspark-operations").getOrCreate()
sc = spark.sparkContext

# Create a RDD from the list
rdd = sc.parallelize(data)
df = spark.createDataFrame(rdd, ['employee_name', 'department', 'country', 'salary', 'age', 'bonus'])

df.show()
df.printSchema()

print("{} Running group by on {} {}".format("-" * 10, "department", "-" * 10))
group_by = df.groupBy("department")
# Min
group_by.min().show()
# Max
group_by.max().show()
# Average
group_by.avg().show()
# Total Salary
group_by.sum().show()

print("{} Running group by on {} {}".format("-" * 10, "country", "-" * 10))
group_by = df.groupBy("country")
# Min
group_by.min().show()
# Max
group_by.max().show()
# Average
group_by.avg().show()
# Total Salary
group_by.sum().show()
