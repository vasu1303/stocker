from dataclasses import dataclass, asdict

@dataclass
class NewsEvent:
    symbol: str
    headline: str
    source: str
    url: str
    published_at: str

    def to_dict(self) -> dict:
        """Converts the Dataclass instance into a standard python dictionary"""
        return asdict(self)