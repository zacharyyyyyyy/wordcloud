# -*- coding: utf-8 -*-
import scrapy
import music163.items
import json
import time



class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ['https://music.163.com/api/v1/resource/comments/R_SO_4_185668?limit=10&&offset=0']
    headers = {
        "Referer": "http://music.163.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
    }
    maxPage=300
    offset=0
    maxOffset = maxPage *10


    def parse(self, response):
        data=json.loads(response.body)
        comments=data['comments']
        self.username = []
        self.text = []
        self.date = []
        self.like = []

        for i in range(0,len(comments)):
            self.username.append(comments[i]['user']['nickname'])
            self.text.append(comments[i]['content'])
            time_local=time.localtime(comments[i]['time']/1000)
            self.date.append(time.strftime("%Y-%m-%d %H:%M:%S",time_local))
            self.like.append(comments[i]['likedCount'])
 #           print("用户名：%s" %comments[i]['user']['nickname'])
 #           print("评论：%s" %comments[i]['content'])
 #           print("评论时间：%s" %time.strftime("%Y-%m-%d %H:%M:%S",time_local))
 #           print("点赞数：%s" %comments[i]['likedCount'])
 #           print("\n")

        item = music163.items.Music163Item()
        item['username'] = self.username
        item['text'] = self.text
        item['date'] = self.date
        item['like'] = self.like
        yield item

        int(self.offset)
        self.offset += 10

        if self.offset<self.maxOffset:
            url=response.urljoin("https://music.163.com/api/v1/resource/comments/R_SO_4_185668?limit=10&&offset="+str(self.offset))
            yield scrapy.Request(url=url, callback=self.parse)

        print("已写入数据："+str(self.offset)+"条数据")


