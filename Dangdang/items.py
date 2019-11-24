# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    #作者
    author=scrapy.Field()
    # 书名称
    book_name = scrapy.Field()
    #价格
    price=scrapy.Field()
    #定价
    pricing=scrapy.Field()
    #评论人数
    comment_num=scrapy.Field()
    #出版社
    press=scrapy.Field()
    #出版时间
    press_time=scrapy.Field()

