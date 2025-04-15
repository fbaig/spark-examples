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
        .appName("PythonWordCount")\
        .getOrCreate()

    # (2) Create RDD
    lines = spark.read.text(sys.argv[1]).rdd \
                                        .map(lambda r: r[0]) # Transformation

    # (3) Transformations
    counts = lines.flatMap(lambda x: x.split(',')) \
                  .map(lambda x: (x, 1)) \
                  .reduceByKey(add)
    # (4) Action
    output = counts.collect()
    for (word, count) in output:
        print("%s: %i" % (word, count))

    spark.stop()
