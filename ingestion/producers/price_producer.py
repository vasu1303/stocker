from producers.base_producer import BaseProducer
from models.price import PriceEvent
from config.settings import PRICE_TOPIC
import logging

logger = logging.getLogger(__name__)

class PriceProducer(BaseProducer):
    def publish(self, event: PriceEvent) -> None:
        """Publishes a price event to the stock price kafka topic"""
        try:
            self.producer.send(PRICE_TOPIC, event.to_dict())

            logger.info(f"Published price event for {event.symbol}")


        except Exception as e:
            logger.error(f"Failed to publish price event for {event.symbol} : {e}")

