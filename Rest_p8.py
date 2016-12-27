
# coding: utf-8

# In[4]:

import requests
import re
busstopurl='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016'
data=requests.get(busstopurl).text
print data
p=re.compile('<BUS_STA_NM>(.+?)</BUS_STA_NM>')
res=p.findall(data)
for item in res:
    print item
buspassengers='http://openAPI.seoul.go.kr:8088/sample/xml/CardBusStatisticsService/1/5/201510/7016/'
data=requests.get(busstopurl).text
print data
p=re.compile('<RIDE_PASGR_NUM>(.+?)</RIDE_PASGR_NUM>')
res=p.findall(data)
for item in res:
    print item
    
KEY="694f495468646b73313130676c426659"
TYPE='xml'
SERVICE='CardBusStatisticsService'
START_INDEX=str(1)
END_INDEX=str(5)
USE_MON=str(201512)
BUS_ROUTE_NO=str(7016)
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
url+=USE_MON
url+='/'
url+=BUS_ROUTE_NO
import requests

data=requests.get(url).text
print data

