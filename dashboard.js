// dashboard.js
async function fetchJSON(path){ const r = await fetch(path); return await r.json(); }

async function render() {
  const sentiment = await fetchJSON('/api/sentiment_distribution');
  const trend = await fetchJSON('/api/articles_over_time');
  const recent = await fetchJSON('/api/articles');
  const top = await fetchJSON('/api/top_articles');

  // Sentiment pie
  const ctx = document.getElementById('sentimentChart');
  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: ['Positive','Neutral','Negative'],
      datasets:[{ data: [sentiment.positive, sentiment.neutral, sentiment.negative] }]
    }
  });

  // Trend line
  const trendCtx = document.getElementById('trendChart');
  const dates = trend.map(r => r.date);
  const counts = trend.map(r => r.count);
  new Chart(trendCtx, {
    type: 'line',
    data: { labels: dates, datasets: [{ label: 'Articles', data: counts, fill:false }] },
    options: { scales: { x: { display: true } } }
  });

  // Recent list
  const recentList = document.getElementById('recentList');
  recent.forEach(a => {
    const li = document.createElement('li');
    li.innerHTML = `<a href="${a.url}" target="_blank">${a.title}</a>
      <div style="font-size:0.85em;color:#666">${a.publication || ''} — ${a.published_at ? new Date(a.published_at).toLocaleString() : ''} — ${a.sentiment_label} (${a.sentiment_score.toFixed(2)})</div>`;
    recentList.appendChild(li);
  });

  // Top articles table
  const tbody = document.querySelector('#topTable tbody');
  top.forEach(a => {
    const tr = document.createElement('tr');
    tr.innerHTML = `<td><a href="${a.url}" target="_blank">${a.title}</a></td><td>${a.publication||''}</td><td>${a.sentiment_score.toFixed(2)}</td>`;
    tbody.appendChild(tr);
  });
}

render().catch(e => console.error(e));
