import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from jl_task.items import Smartphone


class TopSmartphonesSpider(CrawlSpider):
    name = 'smartphone_spider'
    start_urls = ['https://ozon.by/category/smartfony-15502/?sorting=rating',
                  'https://ozon.by/category/smartfony-15502/?page=2&sorting=rating',
                  'https://ozon.by/category/smartfony-15502/?page=3&sorting=rating']

    rules = (
        Rule(LinkExtractor(allow='product'), callback='parse_smartphone'),
    )

    def parse_smartphone(self, response):
        os_android = response.xpath('//*[@id="section-characteristics"]').re(r"Android \d{2}")
        os_iphone = response.xpath('//*[@id="section-characteristics"]').re(r"iOS \d{2}")
        os = os_iphone if os_iphone else os_android
        item = Smartphone()
        item['os'] = os[0] if os else 'Unknown version of android'
        yield item
