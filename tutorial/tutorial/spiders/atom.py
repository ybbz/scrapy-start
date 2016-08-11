# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider


class AppleSpider(SitemapSpider):
    name = 'atom'
    sitemap_urls = ['http://www.apple.com/sitemap.xml']
    sitemap_rules = [
        ('/mac/', 'parse_mac'),
        ('/itunes/', 'parse_itunes'),
        ('', 'parse')
    ]

    def parse(self, response):
        self.log("default parsing method for {}".format(response.url))

    def parse_mac(self, response):
        self.log("parse_mac method for {}".format(response.url))

    def parse_itunes(self, response):
        self.log("parse_itunes method for {}".format(response.url))
