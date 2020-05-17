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
    cookie = input('输入你的cookie： ')
    headers = {
                'authority': 'pixon.ads-pixiv.net',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'sec-fetch-dest': 'iframe',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-mode': 'navigate',
                'referer': 'https://www.pixiv.net/',
                'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8',
                'cookie': cookie
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        user_ids = response.xpath('//div[@class="userdata"]/a/@href').extract()
        next_page = response.xpath('//div[@class="_pager-complex"]//li/a/@href')[-1].extract()
        base_first_url = self.start_urls[0].split('?')[0]

        for user_id in user_ids:
            user_id = user_id.split('/')[-1]
            yield scrapy.Request(url='https://www.pixiv.net/ajax/user/{user_id}/profile/all?lang=ja'.format(user_id=user_id),
                                 callback=self.parse_json, headers=self.headers)
        yield scrapy.Request(url=base_first_url + next_page, callback=self.parse, headers=self.headers)

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