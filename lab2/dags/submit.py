from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setAppName("lab2 PySpark App").setMaster("spark://spark-master:7077")
sc = SparkContext(conf=conf)
spark = SparkSession.builder.config(conf=conf).getOrCreate()

data = [("Ivan", 25), ("Natasha", 30), ("Vladimir", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()

spark.stop()
