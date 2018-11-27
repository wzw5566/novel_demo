# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelDemoPipeline(object):
    def process_item(self, item, spider):
        for i in range(1, len(item["nov_chapter"])):
            print(item["nov_chapter"][i])
        return item
