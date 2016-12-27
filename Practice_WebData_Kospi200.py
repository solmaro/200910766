
# coding: utf-8

# In[2]:

import urllib
f=urllib.urlopen("https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=sUjxV8maGYKT0gTOz7qoDA")
mydata=f.read()
import lxml.html
from lxml.cssselect import CSSSelector
html = lxml.html.fromstring(mydata)
sel = CSSSelector('#prices > table')
nodes=sel(html)

len(nodes)
for node in nodes:
    print node.text_content()

