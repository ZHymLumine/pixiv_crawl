# -*- coding: utf-8 -*-
import scrapy
import json
from pixiv.items import PixivItem
import re


class PixivspiderSpider(scrapy.Spider):
    name = 'pixivspider'
    allowed_domains = ['pixiv.net']
    base_url = 'https://www.pixiv.net'
    start_urls = ['https://www.pixiv.net/bookmark.php?type=user&rest=show&p=1']

    def parse(self, response):
        user_ids = response.xpath('//div[@class="userdata"]/a/@href').extract()
        next_page = response.xpath('//div[@class="_pager-complex"]//li/a/@href')[-1].extract()
        base_first_url = self.start_urls[0].split('?')[0]

        for user_id in user_ids:
            user_id = user_id.split('/')[-1]
            yield scrapy.Request(url='https://www.pixiv.net/ajax/user/{user_id}/profile/all?lang=ja'.format(user_id=user_id),
                                 callback=self.parse_json)
        yield scrapy.Request(url=base_first_url + next_page, callback=self.parse)

    def parse_json(self, response):
        dict = json.loads(response.body_as_unicode())
        body = dict['body']
        author_illusts = body['illusts']
        illusts = [key for key, value in author_illusts.items()]
        for illust in illusts:
            illust_url = 'https://www.pixiv.net/artworks/{illust}'.format(illust=illust)
            yield scrapy.Request(url=illust_url, callback=self.parse_img)

    def parse_img(self, response):
        html = response.body.decode('utf-8')
        img_url = re.findall('{"mini":".*?","thumb":".*?","small":".*?","regular":"(.*?)","original":".*?"}', html)
        img_url = img_url[0]
        name = re.findall('"userName":"(.*?)"', html)
        name = name[0]
        name = re.sub('[\/:*?"<>|]', '', name)
        item = PixivItem()
        item['name'] = name
        item['img_url'] = img_url
        yield item
