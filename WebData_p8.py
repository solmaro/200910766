
# coding: utf-8

# In[4]:

get_ipython().run_cell_magic(u'writefile', u'src/ds_web_data_paging.py', u'import scrapy\n\nclass QuoteItem(scrapy.Item):\n    text = scrapy.Field()\n    author = scrapy.Field()\n\nclass QuotesSpider(scrapy.Spider):\n    name = "quotes"\n    start_urls = [\n        \'http://quotes.toscrape.com/page/1/\',\n    ]\n    def parse(self, response):\n        for quote in response.xpath(\'//div[@class="quote"]\'):\n            item = QuoteItem()\n            item[\'text\'] = quote.xpath(\'span[@class="text"]/text()\').extract_first()\n            item[\'author\'] = quote.xpath(\'span/small/text()\').extract_first()\n            print "crawling ",item[\'author\']\n            yield item\n        next_page = response.xpath(\'//li[@class="next"]/a/@href\').extract_first()\n        if next_page:\n            next_page = response.urljoin(next_page)\n            print "--> visiting ",next_page\n            yield scrapy.Request(next_page, callback=self.parse)\n!scrapy runspider src/ds_web_data_paging.py -o src/ds_web_data_paging.json -t json --logfile src/ds_web_data_paging.logfile')

