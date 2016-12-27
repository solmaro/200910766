
# coding: utf-8

# In[2]:

import os
KEY="694f495468646b73313130676c426659"
TYPE='xml'
SERVICE='ListLocaldata470401S'
START_INDEX=str(1)
END_INDEX=str(5)
url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
print url
import requests
data=requests.get(url)
print data.text
print type(data.encode('utf-8'))
import lxml
import lxml.etree
import StringIO

tree=lxml.etree.parse(StringIO.StringIO(data.encode('utf-8')))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text

