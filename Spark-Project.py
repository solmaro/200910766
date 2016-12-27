
# coding: utf-8

# In[1]:

import findspark


# In[2]:

spark_home="C:\Users\HEO\Downloads\spark-1.6.0-bin-hadoop2.6"
print spark_home


# In[3]:

findspark.init(spark_home)
import pyspark
conf=pyspark.SparkConf()
conf = pyspark.SparkConf().setAppName("myAppName")
sc = pyspark.SparkContext(conf=conf)


# In[4]:

sc._conf.get("spark.jars.packages")


# In[5]:

sc._conf.getAll()


# In[9]:

lines = sc.textFile("FP.txt")
wc = lines    .flatMap(lambda x: x.split(' '))


# In[12]:

wc.collect()


# In[13]:

from operator import add
wc = sc.textFile("FP.txt")    .flatMap(lambda x: x.split(' '))    .map(lambda x: (x.lower().rstrip().lstrip().rstrip(',').rstrip('.'), 1))    .reduceByKey(add)


# In[16]:

wc.take(1000)


# In[ ]:



