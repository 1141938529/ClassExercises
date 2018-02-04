import scrapy
import time
from stockSpider.items import stockItem


class StockSpider(scrapy.Spider):
    name = 'stockspider'
    start_urls = ['http://stock.10jqka.com.cn/']

    def parse(self, response):
        stock_list = response.xpath("//div[@id='rzrq']//table[@class='m-table']/tbody/tr/td[2]/a")
        for stock in stock_list:
            stock_name = stock.xpath("./text()").extract()[0]
            link = stock.xpath("./@href").extract()[0]
            stock_id = link.split('/')[-2]
            # print(stock_name + '===============' + link)
            with open("D://PyDownload//stockdata//" + stock_name + '.txt', mode='w', encoding='utf8'):
                pass

            yield scrapy.Request(url=link,
                                 callback=self.get_stock_data,
                                 meta={'stock_name': stock_name, 'base_url': link, 'index': 2})
        pass

    def get_stock_data(self, response):
        print(response.url)
        time.sleep(3)
        data_table = response.xpath("//table[@class='m-table']/tbody/tr")
        # stock_id = response.url.split('/')[6]
        stock_name = response.meta['stock_name']
        f = open("D://PyDownload//stockdata//" + stock_name + '.txt', 'a', encoding='utf8')
        for row in data_table:
            data_list = row.xpath("./td/text()").extract()
            data = ('|+|'.join(data.strip() for data in data_list))
            f.write(data + '\n')
        f.close()
        index = response.meta['index']
        if index > 4:
            return
        url_str = response.meta['base_url'] + "order/desc/page/" + str(index) + "/ajax/1/"
        yield scrapy.Request(url=url_str, callback=self.get_stock_data, meta={
            'stock_name': stock_name, 'base_url': response.meta['base_url'], 'index': index + 1
        })
