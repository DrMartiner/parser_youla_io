import json
import scrapy
import logging
from ..items import YoulaItem


class BaseYoulaSpider(scrapy.Spider):
    name = 'youla_base'
    start_urls = ['https://youla.io/web-api/geo/popular']
    categories = []

    def parse(self, response):
        """ Load cities """
        try:
            cities = json.loads(response.text)
        except Exception as e:
            msg = 'Error at parse cities JSON'
            self.log(msg, logging.WARNING)

            cities = []

        for city in cities:
            for category in self.categories:
                for sub_category in category.get('sub_categories'):
                    url = 'https://youla.io/{}/{}/{}'.format(
                        city['slug'],
                        category['slug'],
                        sub_category['slug'],
                    )
                    meta = dict(
                        city=city,
                        category=category,
                        sub_category=sub_category
                    )
                    yield scrapy.Request(url, meta=meta, callback=self.parse_category)

    def parse_category(self, response):
        meta = dict(
            city=response.meta['city'],
            category=response.meta['category'],
            sub_category=response.meta['sub_category'],
        )

        for url in response.css('ul.product_list > li.product_item > a::attr(href)'):
            yield response.follow(url, self.parse_ad, meta=meta)

        if not response.css('.alert_message__title'):
            url = response.css('._paginator_next_button::attr(href)')[0].root
            yield response.follow(url, self.parse_ad, meta=meta)

    def parse_ad(self, response):
        try:
            raw_data = response.xpath('//script/text()')[0].re("window.__APP_STATE = \{(.*)\}")
            json_data = '{{{}}}'.format(raw_data[0])
            images_data = json.loads(json_data)
        except Exception as e:
            msg = 'Error at parse JSON at {}'.format(response.url)
            self.log(msg, logging.WARNING)

            images_data = None

        images_urls = []
        if images_data:
            for image in images_data['entities'].get('images', []):
                images_urls.append(image['srcs']['original'])

        if images_urls:
            msg = 'Processing {}'.format(response.url)
            self.log(msg, logging.NOTSET)

            yield YoulaItem(
                slug=response.url.split('/')[-1],
                images=images_urls,
                city=response.meta['city']['slug'],
                category=response.meta['category']['slug'],
                sub_category=response.meta['sub_category']['slug'],
            )
