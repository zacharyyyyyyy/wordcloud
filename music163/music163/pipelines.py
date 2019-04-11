# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Music163Pipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='',
            db='scrapytest',
            charset='utf8',
            use_unicode=True
        )
        self.cursor=self.connect.cursor()

    def process_item(self, item, spider):
        try:
            for i in range(0, len(item['username'])):
                self.cursor.execute(
                    "insert into comment(username,text,dateTime,likeCount) value (%s ,%s ,%s ,%s)", (item['username'][i], item['text'][i], item['date'][i], item['like'][i])
                )

        except Exception as error:
            raise error
        self.connect.commit()
        return item

    def close_spider(self, spider):
        self.connect.close()
        self.cursor.close()
