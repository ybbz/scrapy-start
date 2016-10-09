# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    time = scrapy.Field()
    category = scrapy.Field()


class TestItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()


class AtomItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()


class BaiduSearchItem(scrapy.Item):
    pass


class DoubanTopMoviesItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    rank = scrapy.Field()
    star = scrapy.Field()
    rate = scrapy.Field()
