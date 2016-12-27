
# coding: utf-8

# In[1]:

url = 'http://www.bbc.co.uk/sport/football/premier-league/results'
import requests
r=requests.get(url)
_html=r.text
len(_html)
_html.find('table-stats')
def getIndicesOfAllTableStats(string, query):
    listindex=list()
    offset=0
    i = string.find(query, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(query, i + 1)
    return listindex
param1=_html
param2='table-stats'
_indices=getIndicesOfAllTableStats(param1, param2)
print _indices
from scrapy.selector import Selector
nodes=Selector(text=_html).xpath("//table[@class='table-stats']/tbody/tr[@class='report']/td[@class='match-details']/p")
print nodes[0].extract()
for node in nodes:
    home_team = node.xpath("span[@class='team-home teams']/a/text()").extract()
    score = node.xpath("span[@class='score']/abbr/text()").extract()
    away_team = node.xpath("span[@class='team-away teams']/a/text()").extract()
    if home_team and score and away_team:
        home_team = home_team[0].strip()
        score = score[0].strip()
        home_goals = int(score.split('-')[0])
        away_goals = int(score.split('-')[1])
        away_team = away_team[0].strip()
    print home_team, score, home_goals, away_goals, away_team

