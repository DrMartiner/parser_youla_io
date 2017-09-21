# -*- coding: utf-8 -*-

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class YoulaImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        file_path = '{}/{}/{}/{}/{}'.format(
            request.meta.get('city'),
            request.meta.get('category'),
            request.meta.get('sub_category'),
            request.meta.get('slug'),
            request.meta.get('file_name'),
        )
        return file_path

    def get_media_requests(self, item, info):
        for url in item.get('images', []):
            meta = dict(
                slug=item.get('slug'),
                city=item.get('city'),
                category=item.get('category'),
                sub_category=item.get('sub_category'),
                file_name=os.path.basename(url),
            )
            yield scrapy.Request(url=url, meta=meta)
