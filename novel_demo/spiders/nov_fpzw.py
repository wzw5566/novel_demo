# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from novel_demo.items import NovelDemoItem

class NovFpzwSpider(scrapy.Spider):
    name = 'nov_fpzw'
    allowed_domains = ['fpzw.com']
    start_urls = ['https://www.fpzw.com/1']


    def parse(self, response):

        item = NovelDemoItem()
        item["nov_name"] = response.xpath("//div[@id='title']/h2/a/text()").extract()
        #item["nov_chapter_link"] = response.xpath("/dl[@class='book']/dd[5:]/a/@href").extract()
        yield item

        for i in range(2, 100):

            url = "https://www.fpzw.com/" +str(i)

            yield Request(url, callback=self.parse)