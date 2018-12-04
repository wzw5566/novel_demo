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


    # 定义抓取的整体页数
    def start_requests(self):
        url = "https://www.fpzw.com/{0}"
        for i in range(1, 101):
           # yield scrapy.Request(url=url, callback=self.parse)
            yield scrapy.Request(url.format(i),callback=self.parse)

    def parse(self, response):

        item = NovelDemoItem()
        item["nov_name"] = response.xpath("//div[@id='title']/h2/a/text()")[0].extract()
        item["nov_chapter_link"] = response.xpath("//div[@id='opt']//li[@id='bt_1']/a/@href")[0].extract()
        item["nov_desc"] = response.xpath("//div[@class='wright']//p[@class='Text']/text()")[0].extract()
        item["nov_cate"] = response.xpath("//div[@class='wright']//div[@class='winfo']//ul/li[1]/span/text()")[0].extract()
        item["nov_author"] = response.xpath("//div[@id='title']//em/a/text()")[0].extract()
        item["nov_total_click_num"] = response.xpath("//div[@class='abook']//dd[5]/span/text()")[0].extract()
      #  detail_url = response.xpath("//div[@id='opt']//li[@id='bt_1']/a/@href").extract()

        yield item
