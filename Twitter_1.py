
# coding: utf-8

# In[1]:

import oauth2 as oauth


# In[2]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[3]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'twitter4j.properties')
key=getKey(keyPath)


# In[4]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[5]:

client = oauth.Client(consumer, token)


# In[6]:

help(client.request)


# In[7]:

import urllib
url = "https://api.twitter.com/1.1/statuses/update.json"
mybody=urllib.urlencode({'status': 'Hello 21 160924'})
response,content=client.request(url,method='POST',body=mybody)


# In[8]:

print content


# In[9]:

type(content)


# In[11]:

content["created__at"]


# ##### str은 못읽어온다

# In[12]:

content[0:100]


# ###### 이것도 불편해 그래서 포맷을 맞춰줘야함

# In[13]:

json.dumps(content)


# ##### 결국 파일로 써야함

# In[14]:

import io
with io.open('src/ds_twitter_1.json', 'w', encoding='utf8') as json_file:
    data=json.dumps(content, json_file, ensure_ascii=False, encoding='utf8')
    json_file.write(data)


# # t-2 자신의 타임라인 가져오기

# In[15]:

from pymongo import MongoClient


# In[16]:

_mclient=MongoClient()


# In[17]:

_mclient['ds_twitter']


# In[18]:

_db=_mclient.ds_twitter


# In[19]:

_col=_db.home_timeline


# In[20]:

url="https://api.twitter.com/1.1/statuses/home_timeline.json"


# In[21]:

response,content=client.request(url)


# In[22]:

home_timeline=json.loads(content)


# In[23]:

home_timeline[0]['text']


# In[24]:

for tweet in home_timeline:
    print tweet['text']


# In[25]:

print home_timeline


# In[26]:

for tweet in home_timeline:
    print tweet['id'],tweet['text']


# In[27]:

for tweet in home_timeline:
    print tweet['id'],tweet['text']
    _col.insert_one(tweet)
    


# In[ ]:




# In[ ]:



