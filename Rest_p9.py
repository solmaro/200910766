
# coding: utf-8

# In[1]:

import requests
import re
weatherurl='http://openAPI.seoul.go.kr:8088/sample/xml/RealtimeWeatherStation/1/5/'
data=requests.get(weatherurl).text
print data
p=re.compile('<SAWS_TA_AVG>(.+?)</SAWS_TA_AVG>')
res=p.findall(data)
for item in res:
    print item
    
KEY="694f495468646b73313130676c426659"
TYPE='json'
SERVICE='RealtimeWeatherStation'
START_INDEX=str(1)
END_INDEX=str(5)
STN_NM=u'중구'
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
url+=STN_NM

import requests

data=requests.get(url).text
print data

