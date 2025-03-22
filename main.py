import os
from dotenv import load_dotenv
from api_client import APIClient
from json_parser import JsonParser
from export_service import ExportService

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve environment variables
    base_api_url = os.getenv("API_GAMES_URL")
    tables_and_fixtures_api_url = os.getenv("API_TABLES_AND_FIXTURES_URL")

    if not tables_and_fixtures_api_url or not base_api_url:
        print("Error: API URLs are not defined in the .env file.")
        return

    # Initialize services
    api_client = APIClient()
    parser_service = JsonParser()
    export_service = ExportService()

    # Fetch and parse league data
    try:
        json_response = api_client.get(tables_and_fixtures_api_url)
        league_data = parser_service.parse_league(json_response)
        teams_and_stats = parser_service.parse_teams_and_stats(json_response)

        teams_data = teams_and_stats['teams']
        team_stats_by_table_data = teams_and_stats['team_stats_by_table']

        # Export to CSV
        export_service.export_teams(teams_data, league_data.url_name + '_teams.csv')
        print("Teams data exported to teams.csv")

        for table_name, stats_list in team_stats_by_table_data.items():        
            export_service.export_team_stats(stats_list, league_data.url_name + '_' + table_name + '_teams_stats.csv')
        print("Team stats data exported to teams_stats.csv")
    except Exception as e:
        print(f"Error fetching or parsing league data: {e}")

    # Fetch and parse games data
    try:
        games = []
        for schedule_date in range(1, 17):  # Looping through league calendar dates
            endpoint = f"{base_api_url}72_224_3_{schedule_date}?support_b=false"
            response = api_client.get(endpoint)
            games.extend(parser_service.parse_games(response))
            
        # Export to CSV
        export_service.export_games(games, league_data.url_name + '_games.csv')
        print("Games data exported to games.csv")
    except Exception as e:
        print(f"Error fetching or parsing games data: {e}")

if __name__ == "__main__":
    main()