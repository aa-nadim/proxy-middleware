# File: my_scraper/middlewares/proxy_middleware.py
import logging
import random
from typing import Optional, List
from scrapy import Request, Spider

logger = logging.getLogger(__name__)

class RotatingProxyMiddleware:
    def __init__(self, proxy_list: List[str]):
        self.proxy_list = proxy_list
        self.failed_proxies = {}
        logger.info(f'Initialized RotatingProxyMiddleware with {len(proxy_list)} proxies')

    @classmethod
    def from_crawler(cls, crawler):
        proxy_list = crawler.settings.getlist('PROXY_LIST')
        return cls(proxy_list)

    def _get_proxy(self) -> Optional[str]:
        """Get a random proxy from the list"""
        return random.choice(self.proxy_list) if self.proxy_list else None

    def process_request(self, request: Request, spider: Spider) -> None:
        """Assign a proxy to the request"""
        proxy = self._get_proxy()
        if proxy:
            request.meta['proxy'] = proxy
            logger.info(f'Using proxy {proxy} for {request.url}')

    def process_response(self, request: Request, response, spider: Spider):
        """Handle the response and log any failures"""
        proxy = request.meta.get('proxy')
        if proxy:
            if response.status != 200:
                self._log_failure(proxy, f'HTTP {response.status}')
            else:
                logger.info(f'Successful request with proxy {proxy}')
        return response

    def process_exception(self, request: Request, exception, spider: Spider):
        """Handle and log any exceptions"""
        proxy = request.meta.get('proxy')
        if proxy:
            self._log_failure(proxy, str(exception))
            return request

    def _log_failure(self, proxy: str, reason: str) -> None:
        """Log proxy failures"""
        self.failed_proxies[proxy] = self.failed_proxies.get(proxy, 0) + 1
        logger.warning(f'Proxy {proxy} failed. Reason: {reason}. '
                      f'Total failures: {self.failed_proxies[proxy]}')

