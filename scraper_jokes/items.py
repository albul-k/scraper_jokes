# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperJokesItem(scrapy.Item):
    _id = scrapy.Field()
    theme = scrapy.Field()
    text = scrapy.Field()
    rating = scrapy.Field()
