from dataclasses import dataclass

@dataclass
class Team:
    name: str
    short_name: str
    url_name: str
    id: str
    country_id: str
    