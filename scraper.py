import os
from newsapi import NewsApiClient

# Initialize NewsApiClient with your API key
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY', 'your_newsapi_key_here')
newsapi = NewsApiClient(api_key=NEWSAPI_KEY)

def get_trending_news():
    """
    Fetches top headlines from NewsAPI as trending news articles.
    Returns a list of articles with title and description.
    """
    top_headlines = newsapi.get_top_headlines(language='en', page_size=5)
    articles = top_headlines.get('articles', [])
    trending_news = []
    for article in articles:
        title = article.get('title', '')
        description = article.get('description', '')
        url = article.get('url', '')
        trending_news.append({
            'title': title,
            'description': description,
            'url': url
        })
    return trending_news

if __name__ == "__main__":
    news = get_trending_news()
    for idx, article in enumerate(news):
        print(f"{idx+1}. {article['title']}\n{article['description']}\nURL: {article['url']}\n")
