# my_scraper/my_scraper/spiders/example_spider.py

import scrapy
from scrapy import Request
import logging.config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('LOGS/spider.log'),
        logging.StreamHandler()
    ]
)

class ExampleSpider(scrapy.Spider):
    name = 'example_spider'
    start_urls = ['https://www.scrapingcourse.com/ecommerce/']
    
    custom_settings = {
        'ROBOTSTXT_OBEY': True,
        'DOWNLOAD_DELAY': 2,
        'COOKIES_ENABLED': False,
    }
    
    def start_requests(self):
        for url in self.start_urls:
            yield Request(
                url=url,
                callback=self.parse,
                errback=self.handle_error,
                dont_filter=True
            )
    
    def parse(self, response):
        self.logger.info(f'Processing URL: {response.url} with proxy: {response.meta.get("proxy")}')
        yield {
            'url': response.url,
            'title': response.css('title::text').get(),
            'proxy_used': response.meta.get('proxy')
        }
    
    def handle_error(self, failure):
        self.logger.error(f'Request failed: {failure.request.url}')
        self.logger.error(f'Error: {failure.value}')