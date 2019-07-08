#!/bin/sh

SPARK_PATH=/home/ec2-user/spark
if [ ! -d ${SPARK_PATH} ]; then
    mkdir -p ${SPARK_PATH}
fi

# update jdk
sudo yum -y remove java-1.7.0-openjdk*
sudo yum -y remove tzdata-java.noarch
sudo yum -y install java-1.8.0-openjdk*

# download Anaconda
#wget https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh

cd $SPARK_PATH
# download spark
wget http://mirror.bit.edu.cn/apache/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz
tar xvf spark-2.4.3-bin-hadoop2.7.tgz
mv spark-2.4.3-bin-hadoop2.7 spark

#sudo chmod -R 777 ${SPARK_PATH}
