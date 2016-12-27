
# coding: utf-8

# In[1]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d
import os

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)

