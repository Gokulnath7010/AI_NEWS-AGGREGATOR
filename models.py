# models.py
from sqlalchemy import Column, Integer, String, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Publication(Base):
    __tablename__ = 'publications'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    url = Column(String(512))

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String(512))
    url = Column(String(1024), unique=True, index=True, nullable=False)
    publication_id = Column(Integer, ForeignKey('publications.id'))
    publication = relationship('Publication')
    published_at = Column(DateTime)
    content = Column(Text)
    sentiment_score = Column(Float)
    sentiment_label = Column(String(32))
    created_at = Column(DateTime, default=datetime.utcnow)
