import os
import logging

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

BOT_NAME = 'youla'

LOG_LEVEL = logging.INFO

SPIDER_MODULES = ['youla.spiders']
NEWSPIDER_MODULE = 'youla.spiders'

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 32

DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
   'youla.pipelines.YoulaImagePipeline': 1,
}

IMAGES_URLS_FIELD = 'images'
IMAGES_STORE = os.path.join(BASE_DIR, '../..', 'images')
