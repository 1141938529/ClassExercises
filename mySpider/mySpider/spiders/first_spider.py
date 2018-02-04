import scrapy


class FirstSpider(scrapy.Spider):
    name = 'firstspider'
    start_urls = ['https://www.baidu.com/']

    def parse(self, response):
        print(response.text)
