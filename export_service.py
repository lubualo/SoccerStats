import csv
from typing import List, Dict
from models.team import Team
from models.team_stats import TeamStats
from models.game import Game

class ExportService:
    def export_teams(self, teams: Dict[str, Team], filename: str):
        """
        Export team data to a CSV file.
        :param teams: Dictionary of teams with url_name as keys.
        :param filename: Name of the output file.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Short Name', 'URL Name', 'ID', 'Country ID'])
            for team in teams.values():
                writer.writerow([
                    team.name,
                    team.short_name,
                    team.url_name,
                    team.id,
                    team.country_id
                ])

    def export_team_stats(self, team_stats: List[TeamStats], filename: str):
        """
        Export team statistics to a CSV file.
        :param team_stats: List of team statistics.
        :param filename: Name of the output file.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'Team', 'Games Played', 'Goals', 'Goals Against', 'Wins', 
                'Draws', 'Losses', 'Trend', 'Points', 'Goals Difference'
            ])
            for stats in team_stats:
                writer.writerow([
                    stats.team,
                    stats.game_played,
                    stats.goals,
                    stats.goals_against,
                    stats.wins,
                    stats.draws,
                    stats.losses,
                    ','.join(str(t.value) for t in stats.trend),  # Serialize trend values
                    stats.getPoints(),
                    stats.getGoalsDifference()
                ])

    def export_games(self, games: List[Game], filename: str):
        """
        Export game data to a CSV file.
        :param games: List of game objects.
        :param filename: Name of the output file.
        """
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                'ID', 'Stage Round Name', 'Status', 'Local', 'Visitor', 
                'Local Score', 'Visitor Score', 'Local Red Cards', 
                'Visitor Red Cards', 'Date'
            ])
            for game in games:
                writer.writerow([
                    game.id,
                    game.stage_round_name,
                    game.status,
                    game.local,
                    game.visitor,
                    game.local_score,
                    game.visitor_score,
                    game.local_red_cards,
                    game.visitor_red_cards,
                    game.date.strftime('%Y-%m-%d %H:%M') if game.date else None
                ])
