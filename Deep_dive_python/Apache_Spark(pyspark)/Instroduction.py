# import pyspark
# import pandas as pd
# f = print(pd.read_excel('D:\Python_Revised_notes\Apache_Airflow\Book.xlsx'))
# print(f) 

# ========================================================

from pyspark.sql import SparkSession

path = 'D:\Python_Revised_notes\Apache_Airflow\Book.xlsx'
spark = SparkSession.builder.appName('test').getOrCreate()
df_pyspark = spark.read.execl(path)
print(df_pyspark)
