from dotenv import load_dotenv
import os

load_dotenv()

# KAFKA

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
PRICE_TOPIC = os.getenv("PRICE_TOPIC", "stock-prices")
NEWS_TOPIC = os.getenv("NEWS_TOPIC", "stock-news")

# NEWS-API

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# WATCHLIST

WATCHLIST = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "WIPRO.NS"
]

PRICE_FETCH_INTERVAL = 60
NEWS_FETCH_INTERVAL = 300
