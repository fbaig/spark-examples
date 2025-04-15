#!/bin/bash

LOCAL_DATA_PATH="$(pwd)/data/"
LOCAL_CODE_PATH="$(pwd)/"

#NAME=apache/spark-py:v3.2.1
NAME=apache/spark-py:v3.4.0

## To locally test spark-java ##
# /opt/spark/bin/spark-submit --class SparkWordCount target/Spark-Demo-cse532-1.0.jar /data/word-count.csv /data/out
#
## GCP does not support --class ##
# /opt/spark/bin/spark-submit target/Spark-Demo-cse532-1.0.jar /data/word-count.csv /data/out
#NAME=apache/spark:3.5.5-java17

## To compile spark-java ##
#NAME=maven:latest


docker run -it \
       --user root \
       -v "$LOCAL_DATA_PATH":/data/ \
       -v "$LOCAL_CODE_PATH":/code/ \
       $NAME bash
