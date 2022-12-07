# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:08:51 2021

@author: Gökhan Akay
"""

import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName("GokhanAppDeneme").getOrCreate()

rdd = spark.sparkContext.parallelize([1,2,3,4,5])
rdd.count()
