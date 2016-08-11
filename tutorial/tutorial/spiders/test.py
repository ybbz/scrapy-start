# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TestItem


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["test.com"]
    start_urls = (
        'http://www.test.com/',
    )

    def parse(self, response):
        sel = scrapy.Selector(response)
        for h3 in response.xpath('//h3').extract():
            yield TestItem(name=h3)

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)
