import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///test.db')
Session = sessionmaker(bind=engine)

from models import Article
from mybase import Session, Base

Base.metadata.create_all(engine)
# 3 - create a new session
session = Session()


article = Article(title='Some title', author='me')
session.add(article)
session.commit()

