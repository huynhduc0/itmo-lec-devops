from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySparkApp").master("spark://spark-master:7077").getOrCreate()

print("Spark Configuration:")
for key, value in spark.sparkContext.getConf().getAll():
    print(f"{key} : {value}")

data = [("Ivan", 25), ("Natasha", 30), ("Vladimir", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.show()
average_age = df.agg({"Age": "avg"}).collect()[0][0]
print(f"Average age: {average_age}")

spark.stop()
