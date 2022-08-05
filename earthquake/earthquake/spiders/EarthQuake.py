import json
import sys

import scrapy
from fake_useragent import UserAgent

sys.path.append("..")
from earthquake.items import EarthquakeItem

'''
scrapy demo for earthquake info
run: scrapy crawl EarthQuake
run and save to a file: scrapy crawl EarthQuake -o data.json -t json
'''


class EarthquakeSpider(scrapy.Spider):
    name = 'EarthQuake'
    ua = UserAgent()

    # allowed_domains = ['news.ceic.ac.cn']
    # start_urls = ['http://news.ceic.ac.cn/']

    def start_requests(self):
        for i in range(1, 100):
            print('The %dth page' % i)
            headers = {'user-agent': self.ua.random}
            yield scrapy.Request(
                f'http://www.ceic.ac.cn/ajax/search?page={i}&&start=&&end=&&jingdu1=&&jingdu2=&&weidu1=&&weidu2=&&height1=&&height2=&&zhenji1=&&zhenji2=&&callback=jQuery180019825776782252214_1659582825277&_=1659582846338',
                headers=headers)

    def parse(self, response):
        j = response.text[42: -1]
        json_text = json.loads(j)
        data = json_text.get('shuju')
        for i in data:
            if float(i.get('M')) > 5:
                item = EarthquakeItem()
                item['level'] = i.get('M')
                item['o_time'] = i.get('O_TIME')
                item['latitude'] = i.get('EPI_LAT')
                item['longitude'] = i.get('EPI_LON')
                item['depth'] = i.get('EPI_DEPTH')
                item['location'] = i.get('LOCATION_C')
                yield item
