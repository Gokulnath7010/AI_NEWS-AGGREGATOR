CREATE DATABASE IF NOT EXISTS ai_news;
USE ai_news;

CREATE TABLE IF NOT EXISTS publications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  url VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS articles (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(512),
  url VARCHAR(1024) NOT NULL UNIQUE,
  publication_id INT,
  published_at DATETIME,
  content TEXT,
  sentiment_score FLOAT,
  sentiment_label VARCHAR(32),
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (publication_id) REFERENCES publications(id)
);
