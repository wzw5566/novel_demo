# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nov_name = scrapy.Field()
    nov_author = scrapy.Field()
    nov_chapter = scrapy.Field()
    nov_chapter_link = scrapy.Field()
    nov_chapter_text = scrapy.Field()
    nov_desc = scrapy.Field()
    nov_cate = scrapy.Field()
    #总点击量
    nov_total_click_num = scrapy.Field()
    #本月点击量
    nov_month_click_num = scrapy.Field()
    #本周点击量
    nov_weak_click_num = scrapy.Field()
    #作品性质
    nov_nature = scrapy.Field()
    #完结情况
    nov_conclusion = scrapy.Field()
    #授权状态
    nov_authorization_status = scrapy.Field()
    #首发状态
    nov_first_state = scrapy.Field()

