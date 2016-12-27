
# coding: utf-8

# In[1]:

import oauth2 as oauth
def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d
import os

keyPath=os.path.join(os.getcwd(), 'src', 'twitter4j.properties')
key=getKey(keyPath)
import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])
client = oauth.Client(consumer, token)


# In[2]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
prev_id=None
f=open('FP.txt','a')
for i in range(0,20):
    myparam={'q':'particles','count':10,'max_id':prev_id}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        f.write(json.dumps([str(i),tweet['text']]))
        f.write("\n")
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()


# In[3]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
prev_id=None
f=open('FP.txt','a')
for i in range(0,20):
    myparam={'q':'particles','count':10,'max_id':811741310201700351}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        f.write(json.dumps([str(i),tweet['text']]))
        f.write("\n")
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()


# In[4]:

import urllib
url = "https://api.twitter.com/1.1/search/tweets.json"
prev_id=None
f=open('FP.txt','a')
for i in range(0,20):
    myparam={'q':'particles','count':10,'max_id':811736906904043520}
    mybody=urllib.urlencode(myparam)
    response, content = client.request(url+"?"+mybody, method="GET")
    tsearch_json = json.loads(content)
    print len(tsearch_json['statuses'])
    for i,tweet in enumerate(tsearch_json['statuses']):
        f.write(json.dumps([str(i),tweet['text']]))
        f.write("\n")
    prev_id=int(tsearch_json['statuses'][-1]['id'])-1
    print prev_id
f.close()


# In[ ]:



