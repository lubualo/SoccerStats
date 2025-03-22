from dataclasses import dataclass
from datetime import datetime

@dataclass
class Game:
    id: str
    stage_round_name: str
    status: str
    local: str
    visitor: str
    local_score: int
    visitor_score: int
    local_red_cards: int
    visitor_red_cards: int
    date: datetime

    def was_played(self) -> bool:
        """
        Check if the game has been played based on its status.
        If `status` is "Prog.", it means the game is scheduled but not played.
        """
        return self.status != "Prog."
