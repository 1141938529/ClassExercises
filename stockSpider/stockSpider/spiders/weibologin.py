import scrapy


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    # start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {},
        'DOWNLOADER_MIDDLEWARES': {},
    }

    def start_requests(self):
        yield scrapy.FormRequest(
            url='',
            formdata='',
            headers='',
            callback=self.parse,
        )

    def parse(self, response):
        print(response.text)
        pass
