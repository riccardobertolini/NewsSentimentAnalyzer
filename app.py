from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import requests
from dotenv import load_dotenv
import os
import nltk

# Load environment variables from .env file (API for newsapi.org)
load_dotenv()

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Create the Flask application instance / backend server
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# This is the route for analyzing the news sentiment
@app.route('/analyze', methods=['POST'])
def analyze():
    keyword = request.form['keyword']
    articles, sentiment_scores = get_news_sentiment(keyword)
    zipped_results = list(zip(articles, sentiment_scores))
    return render_template('results.html', keyword=keyword, results=zipped_results)


# This function is used on the frontend, templates/result.html to get the maximum value in an iterable
@app.template_filter('max')
def find_max(iterable):
    return max(iterable)


# This function is used on the frontend, templates/result.html to get the maximum value in an iterable
def get_news_sentiment(keyword):
    articles = []
    sentiment_scores = []
    api_key = os.getenv('NEWSAPI_KEY')
    url = f'https://newsapi.org/v2/everything?q={keyword}&sortBy=date&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    articles_data = data.get('articles')
    if articles_data:
        for article_data in articles_data:
            article_title = article_data.get('title')
            article_text = article_data.get('description')
            if article_title and article_text:
                articles.append({'title': article_title, 'text': article_text})
                sid = SentimentIntensityAnalyzer()
                sentiment_scores.append(sid.polarity_scores(article_text))
    return articles, sentiment_scores


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
