import scrapy


class YoulaItem(scrapy.Item):
    slug = scrapy.Field()
    images = scrapy.Field()
    city = scrapy.Field()
    category = scrapy.Field()
    sub_category = scrapy.Field()
