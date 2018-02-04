import scrapy
from scrapy.linkextractors import LinkExtractor
import time
import re


class BookSpider(scrapy.Spider):
    name = 'book'

    custom_settings = {
        "ITEM_PIPELINES" : {}
    }

    start_urls = ["http://www.quanwenyuedu.io/"]

    def parse(self, response):
        # book_link = LinkExtractor(allow=r".quanwenyuedu.io$", deny=r'big')
        book_link = LinkExtractor(allow=r".quanwenyuedu.io$", deny=r'big').extract_links(response)
        text_link = LinkExtractor(allow=r"/(\d+).html$", deny=r'big').extract_links(response)

        for one_book in book_link:
            yield scrapy

    # 不用 parse
    # def parse(self, response):

    def do_book(self, response):

        info_list = response.xpath("//div[@class='top']//span//text()").extract()

        file_name = "/root/PycharmProjects/spider/myspider/files/" + response.url.split('/')[2].split('.')[0]
        with open(file_name, 'w') as f:
            # print('\n'.join(info_list))
            f.write('\n'.join(info_list)+'\n\n')

        # print("================================")
        time.sleep(2)

    def do_info(self, response):
        # print(response.text)
        info = re.compile("setTimeout.*").search(response.text).group()
        # print('info : ', info)
        id = info.split("','")[3]
        sky = info.split("','")[5]
        t = info.split("','")[7].split("'")[0]

        form_info = {
            'a' : 'ajax',
            'c' : 'book',
            'id' : id,
            'sky' : sky,
            't' : t,
            '_type' : 'ajax',
            'rndval' : str(int(time.time()*1000))
        }

        print(form_info)

        url_str= response.url.rsplit('/',1)[0] + '/index.php?c=book&a=ajax'
        print("url_str : ", url_str)
        yield scrapy.FormRequest(
            url=url_str,
            formdata=form_info,
            callback=self.do_text
        )

    def do_text(self, response):
        print(response.url)
        # print(response.text)

        time.sleep(1)

        text_list = response.xpath("//p/text()").extract()
        # print('\n'.join(text_list)+'\n===========================================\n')

        file_name = "/root/PycharmProjects/spider/myspider/files/" + response.url.split('/')[2].split('.')[0]
        # print("file_name : ", file_name)
        with open(file_name, 'a') as f:
            f.write('\n'.join(text_list)+'\n===========================================\n')