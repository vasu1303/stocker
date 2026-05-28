import yfinance as yf
import logging
from datetime import datetime, timezone
from models.price import PriceEvent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_price(symbol: str) -> PriceEvent | None:
    """
        Fetches the current price tick for a given NSE stock symbol.
        Returns a PriceEvent instacne or None if the fetch fails
    """

    try: 
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info

        current_price = info.last_price
        volume = info.last_volume

        if current_price is None:
            logger.warning(f"No Price data returned for {symbol}")
            return None
        
        return PriceEvent(
            symbol=symbol,
            current_price=float(current_price),
            volume=int(volume) if volume else 0,
            timestamp=datetime.now(timezone.utc).isoformat()
        )
    
    except Exception as e:
        logger.error(f"Failed to fetch price for {symbol}: {e}")
        return None
    

