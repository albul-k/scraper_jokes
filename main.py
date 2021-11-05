from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scraper_jokes import settings
from scraper_jokes.spiders.anekdotme import AnekdotmeSpider


if __name__ == '__main__':
    crawl_settings = Settings()
    crawl_settings.setmodule(settings)
    crawl_proc = CrawlerProcess(settings=crawl_settings)
    crawl_proc.crawl(
        AnekdotmeSpider,
    )
    crawl_proc.start()
