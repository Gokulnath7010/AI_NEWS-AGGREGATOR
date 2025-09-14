# app.py
from flask import Flask, render_template, jsonify
from db import init_db, SessionLocal
from models import Article, Publication
from sqlalchemy import func
from datetime import datetime

app = Flask(__name__, template_folder="templates", static_folder="static")
init_db()

def row_to_dict(article):
    return {
        "id": article.id,
        "title": article.title,
        "url": article.url,
        "publication": article.publication.name if article.publication else None,
        "published_at": article.published_at.isoformat() if article.published_at else None,
        "sentiment_score": article.sentiment_score,
        "sentiment_label": article.sentiment_label
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/articles")
def api_articles():
    session = SessionLocal()
    rows = session.query(Article).order_by(Article.published_at.desc()).limit(50).all()
    return jsonify([row_to_dict(r) for r in rows])

@app.route("/api/sentiment_distribution")
def api_sentiment_distribution():
    session = SessionLocal()
    q = session.query(Article.sentiment_label, func.count(Article.id)).group_by(Article.sentiment_label).all()
    result = {label: count for label, count in q}
    # ensure keys present
    for k in ["positive", "neutral", "negative"]:
        result.setdefault(k, 0)
    return jsonify(result)

@app.route("/api/articles_over_time")
def api_articles_over_time():
    session = SessionLocal()
    # group by date
    q = session.query(func.date(Article.published_at), func.count(Article.id)).group_by(func.date(Article.published_at)).order_by(func.date(Article.published_at)).all()
    return jsonify([{"date": str(row[0]), "count": row[1]} for row in q])

@app.route("/api/top_articles")
def api_top_articles():
    session = SessionLocal()
    rows = session.query(Article).order_by(Article.sentiment_score.desc()).limit(10).all()
    return jsonify([row_to_dict(r) for r in rows])

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from db import SessionLocal
from models import Article
session = SessionLocal()
print("Articles:", session.query(Article).count())
