from newsapi import NewsApiClient
from dotenv import load_dotenv
from models.news import NewsEvent
from datetime import datetime, timezone
import logging

import os

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_news(symbol: str) -> list[NewsEvent] | None:
    """
    Fetches the latest real-time and historical news
    """

    try:
        query = symbol.replace(".NS", "")
        newsapi = NewsApiClient(api_key = NEWS_API_KEY)

        response = newsapi.get_everything(
            q=query,
            language = 'en',
            sort_by = 'publishedAt',
            page_size = 5
        )

        articles = response.get("articles", [])

        news_events = []
        for article in articles:
            news_events.append(NewsEvent(
                symbol=symbol,
                headline=article.get("title", ""),
                source=article["source"]["name"],
                url=article.get("url", ""),
                published_at=article.get("publishedAt", ""),
            ))

        return news_events

    except Exception as e:
        logger.error(f"Failed to fetch news for {symbol} : {e}")
        return []