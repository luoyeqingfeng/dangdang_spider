# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from .settings import *

class DangdangPipeline(object):
    def process_item(self, item, spider):
        return item

#mongdb数据库
class MongoPipeline(object):
    def open_spider(self,spider):
        self.conn=MongoClient(MONGO_HONST,27017)
        self.db=self.conn[DB_NAME]
        self.myset=self.db[DB_SET]

    def process_item(self, item, spider):
        print(dict(item))
        self.myset.insert_one(dict(item))
        print("插入成功")
        return item

    def conls_spider(self,spider):
        self.conn.close()
