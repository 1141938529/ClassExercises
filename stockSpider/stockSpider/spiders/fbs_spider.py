import scrapy
# from scrapy.spiders import CrawlSpider,Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.linkextractors import LinkExtractor
import subprocess
import time


# class BizhiSpider(CrawlSpider):
class BizhiSpider(RedisCrawlSpider):
    name = 'bizhi'

    # start_urls = ["http://desk.zol.com.cn/"]
    redis_key = 'bizhi_key'

    bizhi_links = LinkExtractor(allow=r"/bizhi/.*.html")

    rules = (
        Rule(bizhi_links, callback='download_img', follow=True),
    )

    def download_img(self, response):
        img_url = response.xpath("//img[@id='bigImg']/@src").extract()[0]
        print(img_url)

        subprocess.Popen(["wget", img_url, "-P", "/root/PycharmProjects/spider/myspider/files"])
        time.sleep(2)
