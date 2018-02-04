# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class StockspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class StockPipeline(object):
    def __init__(self):
        self.coon = pymysql.Connect(port=3306, host='127.0.0.1', user='root',
                                    password="123456", db='scrapy_stock', charset='utf8')
        self.cursor = self.coon.cursor()

    def process_item(self, item, spider):
        sql = "insert into stock_table(xuhao,jysj,rz_ye,rz_mr,rz_ch,rz_jmr,rq_yl,rq_mc,rq_ch,rq_jmc,rzqye) " \
              "VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
              (item['xuhao'], item['jysj'], item['rz_ye'], item['rz_mr'], item['rz_ch'], item['rz_jmr'], item['rq_yl'],
               item['rq_mc'], item['rq_ch'], item['rq_jmc'], item['rzqye'])
        print(sql)
        self.cursor.execute(sql)
        # return item

    def __del__(self):
        self.cursor.execute('commit')
        self.cursor.close()
        self.coon.close()
