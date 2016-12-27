import os
KEY="694f495468646b73313130676c426659"
TYPE='json'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'
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
url+=LINE_NUM
print url
import requests
data=requests.get(url)
print data.text
import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item
import xml.etree.ElementTree as ET
tree=ET.fromstring(data.encode('utf-8'))
stds=tree.findall('row')
for elements in stds:
    for elm in elements:
        print elm.text
import lxml
import lxml.etree
import StringIO

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text