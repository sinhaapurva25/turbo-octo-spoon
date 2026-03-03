# bigdata
Big Data practice - Spark, Scala, SQL, Spark Streaming

## setps to run a Scala object
cd c:\myWork\bigdata
scalac -classpath "%SPARK_HOME%\jars\*" UDFPractice.scala
jar cf UDFPractice.jar UDFPractice*.class
spark-submit --class UDFPractice UDFPractice.jar

## python venv
cd c:\myWork\bigdata
python -m venv BigDataVenv
BigDataVenv\Scripts\activate
pip install -r requirements.txt
deactivate

Java JDK: https://adoptium.net/temurin/releases/?version=11&os=any&arch=any
Spark: https://archive.apache.org/dist/spark/spark-3.4.1/spark-3.4.1-bin-hadoop3.tgz
Scala: https://www.scala-lang.org/download/2.12.18.html
Hadoop: https://github.com/cdarlint/winutils/tree/master/hadoop-3.3.6/bin

## setps to run a Python file
python MyApp.py Arg1 Arg2

## setps to run a file that has spark submit
spark-submit MyApp.py


## versions of Java, Python, ScALA AND PySpark:
openjdk version "11.0.29" 2025-10-21
OpenJDK Runtime Environment Temurin-11.0.29+7 (build 11.0.29+7)
OpenJDK 64-Bit Server VM Temurin-11.0.29+7 (build 11.0.29+7, mixed mode)
