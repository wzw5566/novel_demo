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
