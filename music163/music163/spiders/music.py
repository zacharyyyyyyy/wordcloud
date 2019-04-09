# -*- coding: utf-8 -*-
import scrapy
import music163.items


class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/#/song?id=185668']
    headers = {
        "Referer": "http://music.163.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3067.6 Safari/537.36",
    }

    def parse(self, response):
       username=response.xpath('//div[@class="itm"]/div[2]/div[1]/div/text()').extract()
       print(username)
