import scrapy
import time
from stockSpider.items import stockItem


class StockSpider(scrapy.Spider):
    name = 'stockspider2'
    start_urls = ['http://stock.10jqka.com.cn/']
    stock_data = stockItem()
    custom_settings = {
        'ITEM_PIPELINES': {'stockSpider.pipelines.StockPipeline': 100, },
    }

    def parse(self, response):
        stock_list = response.xpath("//div[@id='rzrq']//table[@class='m-table']/tbody/tr/td[2]/a")
        for stock in stock_list:
            stock_name = stock.xpath("./text()").extract()[0]
            link = stock.xpath("./@href").extract()[0]
            stock_id = link.split('/')[-2]
            # print(stock_name + '===============' + link)
            # with open("D://PyDownload//stockdata//" + stock_name + '.txt', mode='w', encoding='utf8'):
            #     pass

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
        for row in data_table:
            data_list = row.xpath("./td/text()").extract()
            self.stock_data['xuhao'] = data_list[0].strip()
            self.stock_data['jysj'] = data_list[1].strip()
            self.stock_data['rz_ye'] = data_list[2].strip()
            self.stock_data['rz_mr'] = data_list[3].strip()
            self.stock_data['rz_ch'] = data_list[4].strip()
            self.stock_data['rz_jmr'] = data_list[5].strip()
            self.stock_data['rq_yl'] = data_list[6].strip()
            self.stock_data['rq_mc'] = data_list[7].strip()
            self.stock_data['rq_ch'] = data_list[8].strip()
            self.stock_data['rq_jmc'] = data_list[9].strip()
            self.stock_data['rzqye'] = data_list[10].strip()
            yield self.stock_data
        index = response.meta['index']
        if index > 4:
            return
        url_str = response.meta['base_url'] + "order/desc/page/" + str(index) + "/ajax/1/"
        yield scrapy.Request(url=url_str, callback=self.get_stock_data, meta={
            'stock_name': stock_name, 'base_url': response.meta['base_url'], 'index': index + 1
        })
