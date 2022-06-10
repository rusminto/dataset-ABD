import pyspark
from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.appName('app').getOrCreate()

rawData = pd.read_csv("./../Data BMI.csv")


from pyspark.sql.types import *
mySchema = StructType([ StructField("Subjek", IntegerType(), True),
        StructField("BMI", StringType(), True),
        StructField("Sistol Awal", IntegerType(), True),
        StructField("Sistol 5 menit", IntegerType(), True),
        StructField("Sistol 10 menit", IntegerType(), True),
        StructField("Sistol 15 menit", IntegerType(), True),
        StructField("Rerata Sistol", IntegerType(), True),
        StructField("Diastol Awal", IntegerType(), True),
        StructField("Diastol 5 menit", IntegerType(), True),
        StructField("Diastol 10 menit", IntegerType(), True),
        StructField("Diastol 15 menit", IntegerType(), True),
        StructField("Rerata Diastol", IntegerType(), True),
        StructField("Keterangan", StringType(), True),
        StructField("Obese", StringType(), True)
    ])

df = spark.createDataFrame(rawData, schema=mySchema)
df.filter(df["Keterangan"] != "NaN").show()

