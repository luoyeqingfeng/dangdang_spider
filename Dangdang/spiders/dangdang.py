# -*- coding: utf-8 -*-
import scrapy
import time
from urllib import parse
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import *

class DangdangSpider(RedisCrawlSpider):
    name = 'dangdang'
    allowed_domains = ['book.dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "DangdangSpider:start_urls"
    #解析
    def parse(self, response):
        print("****"*100)
        hrefs=response.xpath("""//dl[@class="inner_dl"]//@href""").extract()
        for url in hrefs:
            yield scrapy.Request(url=url,callback=self.get_page,dont_filter=True)

    def get_page(self,response):
        books=response.xpath("""//ul[@class="bigimg"]/li""")
        next_page = response.xpath("""//li[@class="next"]/a/@href""").extract()
        next_none = response.xpath("""//li[@class="next none"]/a/@href""").extract()
        for book in books:
            itme=DangdangItem()
            bk=book.xpath(""".//text()""").extract()
            # print(bk)
            # itme["author"] = bk[9]
            for i in bk:
                itme["book_name"] = bk[1]
                itme["price"] = bk[3]
                itme["pricing"] = bk[5]
                if "评论" in i:
                    itme["comment_num"] = i
                if "出版社" in i:
                    itme["press"] = i
                try:

                    if time.strptime(i.replace("/","").strip(),"%Y-%m-%d") or time.strptime(i.strip(),"%Y-%m-%d"):
                        itme["press_time"] = i.replace("/","")

                except:
                    pass
            yield itme

        if not next_none and len(next_page)>=1:
            print(next_page)
            #拼接url
            url=parse.urljoin(response.url,next_page[0])
            print(url)
            yield scrapy.Request(url=url,callback=self.get_page,dont_filter=True)

