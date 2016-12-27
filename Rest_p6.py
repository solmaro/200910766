
# coding: utf-8

# In[6]:

import os
import requests

KEY="694f495468646b73313130676c426659"
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX=('1')
END_INDEX=('5')
use_mon='201306'



_maxIter=2
_iter=0
while _iter<_maxIter:
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
    url+='/'
    url+=use_mon
    #print _api
    print url
    data=requests.get(url)
    print data.text
    START_INDEX+=('5')
    END_INDEX+=('5')
    _iter+=1

