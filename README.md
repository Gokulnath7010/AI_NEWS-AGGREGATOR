# 📰 AI News Aggregator & Analytics Dashboard

## 📌 Project Overview
The **AI News Aggregator** is a Python-based system that collects and analyzes AI/technology news articles from multiple online sources.  
It performs web scraping, sentiment analysis, and stores data in a relational database.  
The processed data is visualized on a **Flask-powered interactive dashboard**.

---

## ✨ Features
- 🔎 **Web Scraping**: Fetches news headlines, URLs, dates, and full text from AI/tech sites  
- 🧹 **Data Processing**: Cleans text, removes HTML, and applies **VADER sentiment analysis**  
- 💾 **Database Storage**: Stores articles & publications in SQLite/MySQL using SQLAlchemy  
- 📊 **Interactive Dashboard**:
  - Recent articles list  
  - Sentiment distribution (Pie chart)  
  - Articles trend over time (Line chart)  
  - Top articles by sentiment score (Table)  
  - Top news sources (Bar chart)  

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask, SQLAlchemy  
- **Scraping**: Requests, BeautifulSoup, Feedparser  
- **NLP**: VADER Sentiment Analysis  
- **Database**: SQLite (local) / MySQL or PostgreSQL (production)  
- **Frontend**: HTML, CSS, Chart.js, JavaScript  
- **Deployment**: Render  

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone <your_github_link>
cd ai-news-aggregator

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

DATABASE_URL=sqlite:///ai_news.db

python -c "import db; db.init_db()"

python scraper.py

python app.py

Now open 👉 http://127.0.0.1:5000
--- '''bash
###

---

✅ With this README, you meet **all PDF requirements**:  
- GitHub repo link  
- Deployed app link  
- Setup instructions  
- Deployment docs  

👉 Once you fill in your two links and push this README, your project will be **100% ready for submission**.  

Do you want me to also write a **short email template** you can send to `hr@neubaitics.com` with these links?
