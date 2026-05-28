from dataclasses import dataclass, asdict
from datetime import datetime, timezone

@dataclass
class PriceEvent:
    """Class for tracking price"""
    symbol: str 
    timestamp: str

    # Core Price Data
    current_price: float

    # Number of shares traded during this period
    volume: int 

    def to_dict(self) -> dict:
        """Converts the Dataclass instance into a standard python dictionary"""
        return asdict(self)
    







