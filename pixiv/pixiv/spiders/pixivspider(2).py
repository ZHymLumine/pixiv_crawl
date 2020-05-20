# -*- coding: utf-8 -*-
import scrapy
import json
from pixiv.items import PixivItem
import re


class PixivspiderSpider(scrapy.Spider):
    name = 'pixivspider'
    allowed_domains = ['pixiv.net']
    base_url = 'https://www.pixiv.net/ajax/user/{}/following?offset={}&limit=24&rest=show&tag=&lang=ja'
    id = input('输入你的id： ')
    total_num = input('输入你关注的画师总数： ')
    cookie = input('输入你的cookie： ')
    offset = 0
    start_urls = ['https://www.pixiv.net/ajax/user/{}/following?offset=0&limit=24&rest=show&tag=&lang=ja'.format(id)]
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'referer': 'https://www.pixiv.net/',
        'cookie': cookie
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        html = response.body.decode('utf-8')
        user_ids = re.findall('"userId":"(.*?)","userName":".*?","profileImageUrl":".*?"', html)
        user_ids = set(user_ids)
        if (self.offset + 24) < int(self.total_num):
            self.offset += 24
        for user_id in user_ids:
            yield scrapy.Request(url='https://www.pixiv.net/ajax/user/{user_id}/profile/all?lang=ja'.format(user_id=user_id),
                                 callback=self.parse_json, headers=self.headers)
        next_url = self.base_url.format(self.id, self.offset)
        yield scrapy.Request(url=next_url, callback=self.parse, headers=self.headers)

    def parse_json(self, response):
        dict = json.loads(response.body_as_unicode())
        body = dict['body']
        author_illusts = body['illusts']
        illusts = [key for key, value in author_illusts.items()]
        for illust in illusts:
            illust_url = 'https://www.pixiv.net/artworks/{illust}'.format(illust=illust)
            yield scrapy.Request(url=illust_url, callback=self.parse_img, headers=self.headers)

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
