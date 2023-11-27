# Databricks notebook source
# MAGIC %md
# MAGIC #### Spark Context

# COMMAND ----------

from pyspark import SparkConf, SparkContext

# create SparkConf object
conf = SparkConf().setAppName("myApp").setMaster("local[*]")  # use all available logical CPU cores
sc = SparkContext(conf=conf)  # or SparkContext.getOrCreate(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])
rdd.collect()

# get SparkContext settings in Spark 1.x, 2.x
sc.getConf().getAll()
sc.getConf().get("spark.app.name")

# stop SparkContext and restart the driver
sc.stop()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Spark Sessions

# COMMAND ----------

from pyspark.sql import SparkSession

# create Sessions
spark1 = SparkSession.builder.appName("Session1")  # or `SparkSession.builder.appName("Session1").getOrCreate()`
spark2 = SparkSession.builder.appName("Session2") \
    .config("spark.some.setting", "value2") \
    .config("spark.executor.memory", "4g")

# get SparkContext settings in Spark 2.x
spark1.sparkContext.getConf().getAll()
spark2.sparkContext.getConf().get("spark.app.name")

# stop the underlying SparkContext and both sessions `spark1`, `spark2`
spark1.stop()  # == spark1.sparkContext.stop()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Two Sessions with distinct tables [Demo]
# MAGIC
# MAGIC Session: `spark1` , `spark2`

# COMMAND ----------

# create new sessions
spark1 = spark.newSession()
spark2 = spark.newSession()

#  get "spark1" and "spark2" session ids. They are different
print(spark1)
print(spark2)

# get session contexts. They are the same
print(spark1.sparkContext)
print(spark2.sparkContext)

#  create tables in both sessions
spark1.range(100).createOrReplaceTempView("vtable_1")
spark2.range(100).createOrReplaceTempView("vtable_2")

# list all tables in both sessions
spark1.catalog.listTables()  # or `spark1.sql("show tables").show()`
spark2.catalog.listTables()
