from .base import BaseYoulaSpider


class FlatSpider(BaseYoulaSpider):
    name = 'flat'
    categories = [
        {
            'id': 20,
            'slug': 'nedvijimost',
            'sub_categories': [
                {
                    'id': 2001,
                    'slug': 'prodaja-kvartiri',
                },
                {
                    'id': 2002,
                    'slug': 'prodaja-komnati',
                },
                {
                    'id': 2005,
                    'slug': 'arenda-kvartiri',
                },
                {
                    'id': 2006,
                    'slug': 'arenda-komnati',
                },
            ]
        },
    ]
