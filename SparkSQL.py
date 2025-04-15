from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    # (1) Spark Context / Session
    spark = SparkSession\
        .builder\
        .appName("PySparkSQLDemo")\
        .getOrCreate()

    input_data = spark.read.option("header", True).csv(sys.argv[1])

    # number of records in data for every country
    input_data.groupBy('location').count().show()
    # same query with SQL
    spark.sql("select location, COUNT(*) from {df1} group by location", df1=input_data).show()

    # get records where number of deaths were greater than 100
    deaths_100 = input_data.where(col('new_deaths') > 100)

    #get records when number of deaths in China were greated than 100
    deaths_100.where(col('location') == 'China').show()
    #get records when number of deaths in Belgium were greated than 100
    deaths_100.where(col('location') == 'Belgium').show()
    
    spark.stop()
