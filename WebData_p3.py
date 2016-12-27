
# coding: utf-8

# In[3]:

from urllib import urlopen
keyword='python'
resp=urlopen('http://www.google.com/search?q='+keyword+'')
html=resp.read()
len(html)
import re
p=re.compile('.*(error).*')
print p.search(html).group(1)
import webbrowser
webbrowser.open('http://www.google.com/search?q=python')
import requests

resp = requests.head("http://www.google.com")
print resp.status_code, resp.text, resp.headers
import urllib2
class HeadRequest(urllib2.Request):
     def get_method(self):
         return "HEAD"

response = urllib2.urlopen(HeadRequest("http://google.com/index.html"))
print response.info()
print response.geturl()
from urllib import URLopener
URLopener.version
from urllib import FancyURLopener
class MyOpener(FancyURLopener):
    version = 'My new User-Agent'
MyOpener.version
myopener = MyOpener()
page = myopener.open('http://www.google.com/search?q=python')
html=page.read()
import os
f=open('mygoogle.html','w')
f.write(html)
f.close()
import webbrowser
mygoogle='file://'+'localhost'+os.path.join(os.getcwd(), 'mygoogle.html')
print mygoogle
webbrowser.open(mygoogle)
import re

p=re.compile('href="(https://.*?)"')

res=p.findall(html)
print len(res)
for item in res:
    print item[:100]
import urllib2
import urllib
googleurl = 'https://www.google.com/search'
keyValues = {'q' : 'python programming tutorials'}
request = urllib.urlencode(keyValues)
print request
request = request.encode('utf-8') 
req = urllib2.Request(googleurl+'?'+request)
print req

print req.get_full_url()

print req.get_method
import urllib
keyword='Albert_Einstein'
keyword='Python (programming language)'
s = urllib.urlopen('http://en.wikipedia.org/w/index.php?action=raw&title='+keyword).read()
print s[:5000]
import lxml.html
from lxml.cssselect import CSSSelector
import requests

r = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
tree = lxml.html.fromstring(r.text)
sel = CSSSelector('#mw-content-text > div:nth-child(1)')
results = sel(tree)
print results

