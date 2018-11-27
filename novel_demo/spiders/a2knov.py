# -*- coding: utf-8 -*-
import scrapy
from novel_demo.items import NovelDemoItem
from scrapy.http import Request


class A2knovSpider(scrapy.Spider):
    name = '2knov'
    allowed_domains = ['fpzw.com/']
    start_urls = ['https://www.fpzw.com/xiaoshuo/110/110409/']

    def parse(self, response):

        item = NovelDemoItem()

        #item["nov_name"] = response.xpath("/div[@id='bookinfo']/div[@id='title']/h1/text()").extract()
        #item["nov_author"] = response.xpath("/div[@id='bookinfo']/div[@id='title']/address[@class='author']/a/text()").extract()
        item["nov_chapter"] = response.xpath("/dl[@class='book']/dd[5:]/a/text()").extract()
        item["nov_chapter_link"] = response.xpath("/dl[@class='book']/dd[5:]/a/@href").extract()
        yield item

        for i in range(1, len(item["nov_chapter"])):
            url = "https://www.fpzw.com/xiaoshuo/110/110409/." + str(26113012+i) + "html"
            yield Request(url, callback=self.parse())
