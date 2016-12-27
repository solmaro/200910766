
# coding: utf-8

# In[1]:

import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr
type(geostr)
import json
geojson=json.loads(geostr)
type(geojson)

print geojson['ip']
print geojson['country_code']
country=geojson.get('country_code')
print country

import urllib

def GetCountry(ip):
    res=urllib.urlopen("http://freegeoip.net/json/"+ip).read().decode('utf-8')
    resJson=json.loads(res)
    return resJson.get("country_code")
print GetCountry('61.72.147.164')

