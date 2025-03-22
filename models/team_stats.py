from dataclasses import dataclass, field
from typing import List
from models.match_result_type import MatchResultType

@dataclass
class TeamStats:
    team: str  # Reference to the Team's url_name
    game_played: int
    goals: int
    goals_against: int
    wins: int
    draws: int
    losses: int
    trend: List[MatchResultType] = field(default_factory=list)

    def __post_init__(self):
        # Validate that all elements in `trend` are valid `MatchResultType` values
        if not all(isinstance(item, MatchResultType) for item in self.trend):
            raise ValueError("All items in 'trend' must be of type 'MatchResultType'.")

    def getPoints(self) -> int:
        """
        Calculate and return the total points.
        Each win gives 3 points, each draw gives 1 point, and losses give 0 points.
        """
        return self.wins * 3 + self.draws

    def getGoalsDifference(self) -> int:
        """
        Calculate and return the goal difference (goals scored - goals against).
        """
        return self.goals - self.goals_against
