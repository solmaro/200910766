
# coding: utf-8

# In[2]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_rest_subway_mongo.js', u'use ds_rest_subwayPassengers_mongo_db\ndb.db_rest_subway.find({"CardSubwayStatisticsService.row.SUB_STA_NM":"\uac15\ub0a8\uad6c\uccad"})\n!mongo < src/ds_rest_subway_mongo.js')

