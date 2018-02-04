# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class stockItem(scrapy.Item):
    xuhao = scrapy.Field()
    jysj = scrapy.Field()
    rz_ye = scrapy.Field()
    rz_mr = scrapy.Field()
    rz_ch = scrapy.Field()
    rz_jmr = scrapy.Field()
    rq_yl = scrapy.Field()
    rq_mc = scrapy.Field()
    rq_ch = scrapy.Field()
    rq_jmc = scrapy.Field()
    rzqye = scrapy.Field()
    pass
