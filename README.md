# Company-Trend-Analyzer 

Features
- Enter stock ticker, gather tweets until database is full of non-neutral (single ticker) tweets containing the specified ticker
- Returns live sentiment analysis of gathered tweets in pie chart, with percentages and number of tweets analyzed displayed (and updated every 30sec)
- Uses AlphaVantage API to display line graph of stock recent activity, as well as stock price, volume, last day of trading, percent ratio, and more


Instructions

1. pull code from repository

2. pip install -r requirements.txt

3. python manage.py migrate

4. python manage.py runserver
