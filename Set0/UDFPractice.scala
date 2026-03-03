import org.apache.spark.sql.SparkSession

object UDFPractice {
  def main(args: Array[String]): Unit = {

    val spark = SparkSession.builder()
      .appName("SparkTest")
      .master("local[2]")
      .getOrCreate()

    import spark.implicits._

    val df = Seq(
      (1, "Apurva Sinha1"),
      (2, "Apurva Sinha2")
    ).toDF("id", "name")

    df.show(false)

    spark.stop()
  }
}

/**
* cd C:\myWork\bigdata
* scalac -classpath "%SPARK_HOME%\jars\*" UDFPractice.scala
* jar cf UDFPractice.jar UDFPractice*.class
* spark-submit --class UDFPractice UDFPractice.jar
*/