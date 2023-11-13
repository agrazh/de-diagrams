# Databricks notebook source
# MAGIC %md
# MAGIC #### Spark Context

# COMMAND ----------

from pyspark import SparkConf, SparkContext

# create SparkConf object
conf = SparkConf().setAppName("myApp").setMaster("local[*]")
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
spark1 = SparkSession.builder.appName("Session1").getOrCreate()
spark2 = SparkSession.builder.appName("Session2") \
    .config("spark.some.setting", "value2") \
    .config("spark.executor.memory", "4g") \
    .getOrCreate()

# get SparkContext settings in Spark 2.x
spark1.sparkContext.getConf().getAll()
spark2.sparkContext.getConf().get("spark.app.name")

# stop all sessions and SparkContext and restart the driver
spark1.stop()  # == spark1.sparkContext.stop()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Two Sessions with distinct tables [Demo]
# MAGIC
# MAGIC Session: `spark1` , `spark2`

# COMMAND ----------

# MAGIC %scala
# MAGIC // crate new sessions
# MAGIC val spark1 = spark.newSession()
# MAGIC val spark2 = spark.newSession()
# MAGIC
# MAGIC // get "spark1" and "spark2" session ids. They are different
# MAGIC println(spark1)
# MAGIC println(spark2)
# MAGIC
# MAGIC // get session contexts. They are the same
# MAGIC println(spark.sparkContext)
# MAGIC println(new_spark.sparkContext)
# MAGIC
# MAGIC // create tables in both sessions
# MAGIC val df = spark1.range(100).toDF()
# MAGIC df.createOrReplaceTempView("vtable_1")
# MAGIC spark2.range(100).toDF().createOrReplaceTempView("vtable_2")
# MAGIC
# MAGIC // list all tables in both sessions
# MAGIC spark1.catalog.listTables.show()  // or spark.sqlContext.sql("show tables").show()
# MAGIC spark2.catalog.listTables.show()
