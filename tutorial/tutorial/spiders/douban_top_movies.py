import scrapy
from tutorial.items import DoubanTopMoviesItem


#

class Movie250Spider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://movie.douban.com/top250/"
    ]

    def parse(self, response):
        for info in response.xpath('//div[@class="item"]'):
            item = DoubanTopMoviesItem()
            item['title'] = info.xpath('div[@class="pic"]/a/img/@alt').extract()[0]
            item['link'] = info.xpath('div[@class="pic"]/a/@href').extract()[0]
            item['rank'] = info.xpath('div[@class="pic"]/em/text()').extract()[0]
            value = info.xpath('div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/text()').extract()
            item['star'] = value[0]
            item['rate'] = value[1]
            yield item

        # 翻页
        next_page = response.xpath('//span[@class="next"]/a/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse)
