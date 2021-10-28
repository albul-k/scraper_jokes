import scrapy
from ..loader import ScraperJokesLoader


class AnekdotmeSpider(scrapy.Spider):
    name = 'anekdotme'
    allowed_domains = ['anekdotme.ru']
    start_urls = ['http://anekdotme.ru/']
    xpath = {
        'themes': '//div[@id="sidebar"]//a[contains(@href, "anekdoti_")]/@href',
        'pagination': '//div[@id="paginator_first"]/a/@href',
        'joke': '//div[@class="anekdot"]',
        'joke_rating': 'div[@class="a_info"]/div[@class="info_padd"]/*/span/text()',
        'joke_text': 'div[@class="anekdot_text"]/text()',
    }

    def parse(self, response, **kwargs):
        for url in response.xpath(self.xpath['themes']):
            yield response.follow(url, callback=self.jokes_parse)

    def jokes_parse(self, response, **kwargs):
        for joke in response.xpath(self.xpath['joke']):
            loader = ScraperJokesLoader(response=response)
            loader.add_value('theme', response.url.split('/')[-1].replace('anekdoti_',''))
            loader.add_value('text', 
                             [sentence.get() for sentence in joke.xpath(self.xpath['joke_text'])])
            loader.add_value('rating', joke.xpath(self.xpath['joke_rating']).get())
            yield loader.load_item()

        for url in response.xpath(self.xpath['pagination']):
            yield response.follow(url, callback=self.jokes_parse)
