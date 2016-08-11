import scrapy
from tutorial.items import BlogItem


class BlogSpider(scrapy.spiders.Spider):
    name = "blog"
    allowed_domains = ["ybbz.site"]
    start_urls = [
        "http://blog.ybbz.site/"
    ]

    def parse(self, response):
        for sel in response.xpath('//section/article'):
            item = BlogItem()
            header = sel.xpath('header[@class="post-header"]')
            item['title'] = header.xpath('h1/a/text()').extract()
            item['link'] = header.xpath('h1/a/@href').extract()
            item['time'] = header.xpath('div/span[1]/time/text()').extract()
            item['category'] = header.xpath('div/span[2]/span[3]/a/span/text()').extract()
            yield item
