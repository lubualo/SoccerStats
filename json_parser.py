from models.league import League
from models.team import Team
from models.team_stats import TeamStats
from models.match_result_type import MatchResultType
from models.game import Game
from datetime import datetime

class JsonParser:
    def parse_league(self, json_data: dict) -> League:
        league_data = json_data.get("league", {})
        return League(
            name=league_data.get("name"),
            id=league_data.get("id"),
            url_name=league_data.get("url_name"),
            country_id=league_data.get("country_id"),
            country_name=league_data.get("country_name"),
            is_international=league_data.get("is_international"),
        )

    def parse_teams_and_stats(self, json_data: dict) -> dict:
        tables_groups = json_data.get("tables_groups", [])
        teams = {}
        team_stats_by_table = {}  # Dictionary to store team stats, grouped by table name

        for group in tables_groups:
            tables = group.get("tables", [])
            for table in tables:
                table_name = table.get("name", "Unknown Table").replace(' ', '-')
                team_stats_list = []
                rows = table.get("table", {}).get("rows", [])
                for row in rows:
                    # Parse team data
                    entity = row.get("entity", {}).get("object", {})
                    team = Team(
                        name=entity.get("name"),
                        short_name=entity.get("short_name"),
                        url_name=entity.get("url_name"),
                        id=entity.get("id"),
                        country_id=entity.get("country_id"),
                    )

                    # Store the team in the teams dictionary
                    teams[team.url_name] = team

                    # Parse team stats
                    values = {stat.get("key"): stat.get("value") for stat in row.get("values", [])}

                    # Split the "Goals" string into goals scored and goals against
                    goals_scored, goals_against = map(int, values.get("Goals", "0:0").split(":"))

                    # Convert trend values to MatchResultType Enums
                    trend = [MatchResultType(t) for t in values.get("{trend}", [])]

                    team_stats = TeamStats(
                        team=team.url_name,
                        game_played=int(values.get("GamePlayed", 0)),
                        goals=goals_scored,
                        goals_against=goals_against,
                        wins=int(values.get("GamesWon", 0)),
                        draws=int(values.get("GamesEven", 0)),
                        losses=int(values.get("GamesLost", 0)),
                        trend=trend,
                    )

                    # Add the stats to the list
                    team_stats_list.append(team_stats)
                
                # Add the stats list to the dictionary with the table name as the key
                team_stats_by_table[table_name] = team_stats_list


        return {"teams": teams, "team_stats_by_table": team_stats_by_table}
    
    def parse_games(self, json_data: dict) -> list:
        games_data = json_data.get("games", [])
        games = []

        for game in games_data:
            try:
                # Extract relevant data
                game_id = game.get("id")
                stage_round_name = game.get("stage_round_name")
                status = game.get("status", {}).get("short_name", "Unknown")
                teams = game.get("teams", [])
                
                # Assuming first team is local and second is visitor
                local_team = teams[0].get("url_name") if len(teams) > 0 else None
                visitor_team = teams[1].get("url_name") if len(teams) > 1 else None

                # Handle scores based on the game's status
                if status == "Prog.":  # Game not played
                    local_score = 0
                    visitor_score = 0
                else:  # Game has been played
                    local_score = int(game.get("scores", [0])[0])
                    visitor_score = int(game.get("scores", [0])[1])
                
                local_red_cards = int(teams[0].get("red_cards", 0)) if len(teams) > 0 else 0
                visitor_red_cards = int(teams[1].get("red_cards", 0)) if len(teams) > 1 else 0

                # Convert start_time to datetime
                start_time = game.get("start_time", "")
                game_date = datetime.strptime(start_time, "%d-%m-%Y %H:%M") if start_time else None

                # Create Game instance
                parsed_game = Game(
                    id=game_id,
                    stage_round_name=stage_round_name,
                    status=status,
                    local=local_team,
                    visitor=visitor_team,
                    local_score=local_score,
                    visitor_score=visitor_score,
                    local_red_cards=local_red_cards,
                    visitor_red_cards=visitor_red_cards,
                    date=game_date,
                )

                games.append(parsed_game)
            except Exception as e:
                print(f"Error parsing game data: {e}")

        return games
