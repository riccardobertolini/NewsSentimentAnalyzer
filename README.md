# News Sentiment Analyzer

The News Sentiment Analyzer is a web application that allows users to analyze the sentiment of news articles based on a keyword search. It retrieves news articles from the newsapi.org API, performs sentiment analysis using the VADER (Valence Aware Dictionary and sEntiment Reasoner) algorithm, and displays the sentiment analysis results.


![Screenshot 1](https://github.com/riccardobertolini/NewsSentimentAnalyzer/blob/main/img/image1.png?raw=true)

![Screenshot 2](https://github.com/riccardobertolini/NewsSentimentAnalyzer/blob/main/img/image2.png?raw=true)

## Features

- Search news articles by entering a keyword.
- Perform sentiment analysis on the retrieved articles.
- Display sentiment scores and sentiment labels (positive, neutral, negative) for each article.
- Filter articles based on sentiment (positive, neutral, negative).
- Responsive user interface for easy access on different devices.

## Technologies Used

- Python
- Flask (Python web framework)
- HTML/CSS
- JavaScript (frontend)

## Prerequisites

- Python 3.x installed
- Python packages specified in the `requirements.txt` file

## Installation

1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd NewsSentimentAnalyzer`
3. Install the required Python packages: `pip install -r requirements.txt`
4. Register on newsapi.org, create an .env file cloning the .env.example one and put there your token

## Usage

1. Run the Flask development server: `python app.py`
2. Open a web browser and navigate to `http://localhost:5000`
3. Enter a keyword in the search box and click the "Analyze" button.
4. The sentiment analysis results will be displayed, and you can use the filter buttons to view articles based on sentiment.



