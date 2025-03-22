from dataclasses import dataclass

@dataclass
class League:
    name: str
    id: str
    url_name: str
    country_id: str
    country_name: str
    is_international: bool
