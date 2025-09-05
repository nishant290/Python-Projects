import requests
from django.utils.dateparse import parse_datetime
from .models import NewsArticle
from django.conf import settings


API_KEY = settings.NEWS_API_KEY  
URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

def fetch_and_store_news():
    response = requests.get(URL)
    data = response.json()

    for article in data.get("articles", []):
        title = article["title"]
        summary = article.get("description", "")
        source = article["source"]["name"]
        published_at = parse_datetime(article["publishedAt"])

        if not NewsArticle.objects.filter(title=title).exists():
            NewsArticle.objects.create(
                title=title,
                summary=summary,
                source=source,
                published_at=published_at
            )
