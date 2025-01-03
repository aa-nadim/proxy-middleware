import scrapy


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.scrapingcourse.com"]
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]

    def parse(self, response):
        pass
