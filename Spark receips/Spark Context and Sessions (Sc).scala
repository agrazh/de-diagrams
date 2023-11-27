// Databricks notebook source
// MAGIC %md
// MAGIC #### Spark Context

// COMMAND ----------

import org.apache.spark.{SparkContext, SparkConf}

val conf = new SparkConf().setAppName("myApp").setMaster("local[*]")  // use all available logical CPU cores
val sc = SparkContext.getOrCreate(conf)  // or `new SparkContext(conf)`

val rdd = sc.parallelize(Seq(1, 2, 3, 4, 5))
rdd.collect()  // Array[Int] = Array(1, 2, 3, 4, 5)

// get SparkContext settings in Spark 1.x, 2.x
sc.getConf.getAll
sc.getConf.get("spark.app.name")

// stop SparkContext and restart the driver
sc.stop

// COMMAND ----------

// MAGIC %md
// MAGIC #### Spark Sessions

// COMMAND ----------

import org.apache.spark.sql.{SparkSession}

// create Sessions
val spark1 = SparkSession.builder.appName("Session1") // or `SparkSession.builder.appName("Session1").getOrCreate()`
val spark2 = SparkSession.builder.appName("Session2")
  .config("spark.some.setting", "value2")
  .config("spark.executor.memory", "4g")

// Get SparkContext settings in Spark 2.x
// For some reason this doesn't work with `spark1` and `spark2` but works with spark.newSession() (see in the next paragraph)
spark.sparkContext.getConf.getAll
spark.sparkContext.getConf.get("spark.app.name")

// stop the underlying SparkContext and both sessions `spark1`, `spark2`
spark1.stop()  // or `spark1.sparkContext.stop()`

// COMMAND ----------

// MAGIC %md
// MAGIC #### Two Sessions with distinct tables [Demo]
// MAGIC
// MAGIC Session: `spark1` , `spark2`

// COMMAND ----------

// create new sessions
val spark1 = spark.newSession()
val spark2 = spark.newSession()

// get SparkContext settings in Spark 2.x
spark1.sparkContext.getConf.getAll
spark2.sparkContext.getConf.getAll
spark1.sparkContext.getConf.get("spark.app.name")
spark2.sparkContext.getConf.get("spark.app.name")

// get "spark1" and "spark2" session ids - they are different
println(spark1)
println(spark2)

// get sessions context ids - they are the same
println(spark1.sparkContext)
println(spark2.sparkContext)

// create tables in both sessions
spark1.range(100).toDF().createOrReplaceTempView("vtable_1")
spark2.range(100).toDF().createOrReplaceTempView("vtable_2")

// list all tables in both sessions
spark1.catalog.listTables.show()  // or `spark1.sqlContext.sql("show tables").show()`
spark2.catalog.listTables.show()  // or `spark2.sql("show tables").show()`
