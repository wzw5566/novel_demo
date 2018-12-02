# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from novel_demo.items import NovelDemoItem
from scrapy.http import Request


class FpzwSpider(CrawlSpider):
    name = 'fpzw'
    allowed_domains = ['fpzw.com']
   # start_urls = ['http://fpzw.com/']

    def start_requests(self):
        ua = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3' }
        yield Request('https://www.fpzw.com/1/', headers=ua)

    rules = (
        Rule(LinkExtractor(allow='\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        item = NovelDemoItem()
        item["nov_name"] = response.xpath("//div[@id='title']/h2/a/text()").extract()
        #item["nov_chapter_link"] = response.xpath("/dl[@class='book']/dd[5:]/a/@href").extract()
        print(item["nov_name"])
        return item
