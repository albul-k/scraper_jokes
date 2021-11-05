# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models


class ScraperJokesPipeline:

    def __init__(self) -> None:
        self.engine = create_engine('sqlite:///jokes.db')
        models.Base.metadata.create_all(bind=self.engine)
        self.session = sessionmaker(bind=self.engine)

    def process_item(self, item, spider):
        db = self.session()

        joke = models.Joke(
            theme=item['theme'],
            text=item['text'],
            rating=item['rating'],
        )
        db.add(joke)
        db.commit()

        return item
