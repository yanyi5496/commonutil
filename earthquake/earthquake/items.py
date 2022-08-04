# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EarthquakeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy_me.Field()
    # 震级
    level = scrapy.Field()
    # 发震时刻
    o_time = scrapy.Field()
    # 纬度
    latitude = scrapy.Field()
    # 经度
    longitude = scrapy.Field()
    # 深度
    depth = scrapy.Field()
    # 参考位置
    location = scrapy.Field()
