from abc import ABC, abstractmethod
from kafka import KafkaProducer
from config.settings import KAFKA_BOOTSTRAP_SERVERS
import json
import logging

logger = logging.getLogger(__name__)

class BaseProducer(ABC):
    """
    Abstract base class for all Kafka Producers. 
    Handles connections, serialization and cleanup.
    Subclass must implement the Publish() method.
    """

    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS,
            value_serializer = lambda v: json.dumps(v).encode('utf-8')
        )
        logger.info(f"{self.__class__.__name__} connected to Kafka")

    @abstractmethod
    def publish(self, data) -> None:
        """
        Publish a message to a Kafka Topic.
        Must be implemented by every subclass.
        """

        pass

    def close(self) -> None:
        """
        Cleanly shuts down the Kafka Producer.
        Always call this before the program exits.
        """

        self.producer.flush()
        self.producer.close()

        logger.info(f"{self.__class__.__name__} connection closed cleanly")
        