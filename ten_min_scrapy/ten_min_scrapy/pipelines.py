# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import datetime
import os
import sqlite3

class TenMinScrapyPipeline(object):
    _db=None

    @classmethod
    def get_database(cls):
        cls._db=sqlite3.connect(
            os.path.join(os.getcwd(),'ten_min_scrapy.db'))
        cursor=cls._db.cursor()
        cursor.excute(
            'CREATE TABLE IF NOT EXISTS post(\
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                url TEXT UNIQUE NOT NULL, \
                title TEXT NOT NULL, \
                date DATE NOT NULL \
            );')
        return cls._db
    def process_item(self, item, spider):
        return item
