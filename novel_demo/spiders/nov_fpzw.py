# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from novel_demo.items import NovelDemoItem

#定义抓取的整体页数
def start_requests(self):
    for i in range(1, 51):
        url = "https://www.fpzw.com/" + str(i)
        yield scrapy.Request(url, callback=self.pare)


class NovFpzwSpider(scrapy.Spider):

    name = 'nov_fpzw'
    allowed_domains = ['fpzw.com']
    start_urls = ['https://www.fpzw.com/1']


    def parse(self, response):

        item = NovelDemoItem()
        item["nov_name"] = response.xpath("//div[@id='title']/h2/a/text()").extract()
        #item["nov_chapter_link"] = response.xpath("/dl[@class='book']/dd[5:]/a/@href").extract()
        detail_url = response.xpath("//div[@id='opt']//li[@id='bt_1']/a/@href").extract()

        yield item

    def parse_detail(self, response):


        pass
