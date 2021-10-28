from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
)

Base = declarative_base()


class Joke(Base):
    __tablename__ = 'post'
    id = Column(Integer, autoincrement=True, primary_key=True)
    theme = Column(String, unique=False, nullable=False)
    text = Column(String, unique=False, nullable=False)
    rating = Column(Integer, unique=False, nullable=False)
