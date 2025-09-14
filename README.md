# AI_NEWS-AGGREGATOR
AI News Aggregator Dashboard — Built a web application that scrapes AI/tech news from multiple sources, performs sentiment analysis on articles, and visualizes trends with interactive charts. Implemented with Python, Flask, SQLAlchemy, and Chart.js.
# 📰 AI News Aggregator Dashboard

## 📌 Project Overview
The **AI News Aggregator** is a full-stack web application that collects and analyzes AI/technology-related news from multiple online sources.  
It automatically fetches articles, performs sentiment analysis, stores them in a database, and displays insights in an interactive dashboard.

---

## ✨ Features
- 🔎 **News Collection**: Scrapes/RSS feeds from major AI/tech websites  
- 🧹 **Data Processing**: Extracts article content and cleans text  
- 😀 **Sentiment Analysis**: Classifies articles as Positive / Neutral / Negative  
- 💾 **Database Storage**: Articles stored in SQLite/MySQL via SQLAlchemy  
- 📊 **Dashboard**:
  - Sentiment distribution (pie chart)  
  - Articles over time (line chart)  
  - Recent & top articles (list/table)  
  - Top sources (bar chart)  

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask, SQLAlchemy  
- **Scraping**: BeautifulSoup, Feedparser, Requests  
- **NLP**: VADER Sentiment Analyzer  
- **Database**: SQLite (dev) / MySQL or MSSQL (prod)  
- **Frontend**: HTML, CSS, Chart.js, JavaScript  
- **Deployment**: Render / Railway / Heroku  

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ai-news-aggregator.git
cd ai-news-aggregator
