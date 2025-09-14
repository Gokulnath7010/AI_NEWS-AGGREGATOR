# db.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Publication, Article
from datetime import datetime

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///ai_news.db")

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def get_or_create_publication(session, name, url=None):
    pub = session.query(Publication).filter_by(name=name).first()
    if not pub:
        pub = Publication(name=name, url=url)
        session.add(pub)
        session.commit()
        session.refresh(pub)
    return pub

def upsert_article(session, title, url, publication_id, published_at, content, sentiment_score, sentiment_label):
    existing = session.query(Article).filter_by(url=url).first()
    if existing:
        # update stale fields if you want
        existing.title = title
        existing.content = content
        existing.sentiment_score = sentiment_score
        existing.sentiment_label = sentiment_label
        existing.published_at = published_at
        session.commit()
        return existing
    else:
        art = Article(
            title=title,
            url=url,
            publication_id=publication_id,
            published_at=published_at,
            content=content,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label
        )
        session.add(art)
        session.commit()
        session.refresh(art)
        return art
