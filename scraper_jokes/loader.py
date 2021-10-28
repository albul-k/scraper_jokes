from itemloaders.processors import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
import unicodedata

from .items import ScraperJokesItem


def get_as_joined_list(itms):
    return ''.join(itms)

def preprocess_text(itm):
    itm = itm.replace('\r\n','').strip()
    itm = unicodedata.normalize("NFKD", itm)
    itm += '\r\n'
    return itm

def get_as_int(itms):
    return int(itms[0])


class ScraperJokesLoader(ItemLoader):
    default_item_class = ScraperJokesItem
    theme_out = TakeFirst()
    text_in = MapCompose(preprocess_text)
    text_out = get_as_joined_list
    rating_out = get_as_int
