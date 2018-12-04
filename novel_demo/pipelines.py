# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelDemoPipeline(object):

    def process_item(self, item, spider):
        if item["nov_name"] != []:

            print("小说名: "+ item["nov_name"])

            print("作者: "+ item["nov_author"])

            print("描述: "+ item["nov_desc"])

            print("小说分类: " + item["nov_cate"])

            print("总点击量: " + item["nov_total_click_num"])

            print("小说链接地址: " + item["nov_chapter_link"])


            print("-------------")