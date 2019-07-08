#!/bin/sh

HADOOP_PATH=/home/ec2-user/hadoop

if [ ! -d ${HADOOP_PATH} ]; then
    mkdir -p ${HADOOP_PATH}
fi

cd ${HADOOP_PATH}
wget http://mirror.bit.edu.cn/apache/hadoop/common/hadoop-3.2.0/hadoop-3.2.0.tar.gz
tar xvf hadoop-3.2.0.tar.gz
