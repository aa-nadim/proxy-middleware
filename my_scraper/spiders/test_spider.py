# my_scraper/spiders/test_spider.py
import scrapy

class TestSpider(scrapy.Spider):
    name = 'test_spider'
    start_urls = ['http://httpbin.org/ip']  # Test URL that returns IP address
    
    def parse(self, response):
        self.logger.info(f'Response from {response.url}: {response.text}')
        yield {
            'url': response.url,
            'proxy_used': response.meta.get('proxy'),
            'response': response.text
        }