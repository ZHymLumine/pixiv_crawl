# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import shutil


class PixivPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    # 获取settings文件里设置的变量值
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        img_url = item['img_url']
        yield scrapy.Request(img_url)

    def item_completed(self, results, item, info):
        image_path = [x['path'] for ok, x in results if ok]
        img_path = "%s/%s" % (self.IMAGES_STORE, item['name'])
        if not os.path.exists(img_path):
            os.mkdir(img_path)
            # 将文件从默认下路路径移动到指定路径下
        shutil.move(self.IMAGES_STORE + '/' + image_path[0],
                    img_path + "/" + image_path[0][image_path[0].find("full/") + 6:])
        item['image_path'] = img_path + "/" + image_path[0][image_path[0].find("full/") + 6:]
        return item

