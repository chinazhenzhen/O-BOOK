#sqlalchemy 生成数据库
#flask_sqlalchemy
from sqlalchemy import Column,Integer,String

from app.models.base import db

class Book(db.Model):
    #__tablename__ = 'book'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column('author', String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)#unique 加入索引，不能重复
    summary = Column(String(1000))
    image = Column(String(50))
