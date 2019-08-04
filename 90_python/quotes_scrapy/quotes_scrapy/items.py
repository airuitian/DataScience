# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#爬取的主要目标就是从非结构性的数据源提取结构性数据，例如网页。 
#Scrapy提供 Item 类来满足这样的需求。
#Item 对象是种简单的容器，保存了爬取到得数据。
class QuotesScrapyItem(scrapy.Item):
    # 定义了两个字段，内容与tag
    content = scrapy.Field()
    tags = scrapy.Field()
