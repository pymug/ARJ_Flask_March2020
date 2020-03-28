from sqlalchemy import Column, String, Integer, Date

from mybase import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)