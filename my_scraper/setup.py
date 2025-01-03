from setuptools import setup, find_packages

setup(
    name='my_scraper',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = my_scraper.settings']},
    install_requires=[
        'scrapy>=2.11.0',
        'python-dotenv>=1.0.0',
        'requests>=2.31.0',
        'python-socks>=2.4.3',
    ],
)