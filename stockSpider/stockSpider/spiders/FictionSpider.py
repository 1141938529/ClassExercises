import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider, Rule
import time

patten = re.compile(r".*sky','(\w+)'*")

class Fiction(CrawlSpider):
    name = 'fiction'
    start_urls = [
        'http://www.quanwenyuedu.io/'
    ]
    custom_settings = {
        'ITEM_PIPELINES': {}
    }
    link = LinkExtractor(allow=r'quanwenyuedu.io$', deny='big5')
    link_text = LinkExtractor(allow=r'/[\d+].html$', deny='big5')
    rules = {
        Rule(link_extractor=link, callback='do_book', follow=True),
        Rule(link_extractor=link_text, callback='do_text', follow=True)
    }

    def do_book(self, response):
        print('_________________________________-')
        # print(response.text)
        print(response.url)
        book_info = response.xpath("//div[@class='top']//span//text()").extract()
        # with open('D://PyDownload//fiction//' + book_info[0] + '.txt', 'w') as f:
        #     f.write('\n'.join(book_info))
        time.sleep(2)

    def do_text(self,response):
        #  http: / / aoshidanshen.quanwenyuedu.io/1.html
        filename = response.url.split('/')[2].split('.')[0]
        content_list = response.xpath("//div[@id='content']/p/text()").extract()
        sky = patten.match(response).group(1)
        print(sky)


    # def download_text(self,response):