# scraper.py
import feedparser
import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
from db import SessionLocal, init_db, get_or_create_publication, upsert_article
import time

USER_AGENT = "Mozilla/5.0 (compatible; AI-News-Aggregator/1.0; +https://example.com)"
HEADERS = {"User-Agent": USER_AGENT}

# List of RSS feeds for tech/AI. Add or remove feeds as needed.
FEEDS = [
    ("TechCrunch", "https://techcrunch.com/feed/"),
    ("The Verge", "https://www.theverge.com/rss/index.xml"),
    ("VentureBeat", "https://venturebeat.com/feed/"),
]

analyzer = SentimentIntensityAnalyzer()

def extract_full_text(url):
    """Try to extract article text from the URL using common containers."""
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
    except Exception as e:
        print("Failed to fetch:", url, e)
        return ""
    soup = BeautifulSoup(r.text, "lxml")
    # 1) prefer <article>
    article = soup.find("article")
    if article:
        paras = article.find_all("p")
        if paras:
            return "\n\n".join(p.get_text(strip=True) for p in paras)
    # 2) common selectors
    selectors = [".article-content", ".entry-content", ".post-content", ".c-entry-content", "#content"]
    for sel in selectors:
        node = soup.select_one(sel)
        if node:
            paras = node.find_all("p")
            if paras:
                return "\n\n".join(p.get_text(strip=True) for p in paras)
    # 3) fallback: first N <p>
    paras = soup.find_all("p")
    return "\n\n".join(p.get_text(strip=True) for p in paras[:40])

def get_sentiment_label(text):
    vs = analyzer.polarity_scores(text)
    compound = vs["compound"]
    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"
    return compound, label

def parse_entry_published(entry):
    # feedparser may give published_parsed struct
    if 'published_parsed' in entry and entry.published_parsed:
        return datetime(*entry.published_parsed[:6])
    # fallback try published or updated strings
    for k in ['published', 'updated', 'created']:
        if k in entry:
            try:
                return datetime.strptime(entry[k], "%a, %d %b %Y %H:%M:%S %Z")
            except Exception:
                pass
    return None

def run():
    init_db()
    session = SessionLocal()
    for pub_name, feed_url in FEEDS:
        print("Processing feed:", pub_name, feed_url)
        d = feedparser.parse(feed_url)
        pub = get_or_create_publication(session, pub_name, feed_url)
        for entry in d.entries:
            title = entry.get("title", "No title")
            link = entry.get("link")
            published_at = parse_entry_published(entry)
            # Try to get content from feed; fallback to scraping the page
            content = ""
            if 'content' in entry and len(entry.content) > 0:
                content = entry.content[0].value
            elif 'summary' in entry:
                content = entry.summary
            # fetch full article for better sentiment
            full_text = extract_full_text(link)
            if full_text and len(full_text) > 100:
                text_to_analyze = full_text
            else:
                text_to_analyze = BeautifulSoup(content, "lxml").get_text()
            score, label = get_sentiment_label(text_to_analyze or "")
            # store in DB (upsert-like)
            try:
                upsert_article(session, title, link, pub.id, published_at, text_to_analyze, score, label)
                print("Saved:", title)
            except Exception as e:
                print("DB error:", e)
            # be polite with requests
            time.sleep(1)

if __name__ == "__main__":
    run()
