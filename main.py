from scrapy.crawler import CrawlerProcess
from spider import QuotesSpider
from db import init_db

if __name__ == '__main__':
    init_db()
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
