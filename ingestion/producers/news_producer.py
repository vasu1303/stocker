from producers.base_producer import BaseProducer
from config.settings import NEWS_TOPIC
from models.news import NewsEvent

import logging

logger = logging.getLogger(__name__)

class NewsProducer(BaseProducer):
    """Publish the News Event to the News Topic"""
    def publish(self, event: NewsEvent) -> None:
        try:
            self.producer.send(NEWS_TOPIC, event.to_dict())
            logger.info(f"Published Event Successfully to the Topic for {event.symbol}")
        
        except Exception as e:
            logger.error(f"Event Publishing Failed for the symbol {event.symbol} : {e}")

