import os
from dotenv import load_dotenv
from api_client import APIClient
from json_parser import JsonParser

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve the API URL from the environment variables
    tables_and_fixtures_api_url = os.getenv("API_TABLES_AND_FIXTURES_URL")
    if not tables_and_fixtures_api_url:
        print("Error: API_TABLES_AND_FIXTURES_URL is not defined in the .env file.")
        return

    base_api_url = os.getenv("API_GAMES_URL")
    if not base_api_url:
        print("Error: API_GAMES_URL is not defined in the .env file.")
        return

    # Initialize the API client with the API URL
    api_client = APIClient()

    # Fetch data from the API
    try:
        json_response = api_client.get(tables_and_fixtures_api_url)
    except Exception as e:
        print(f"Error fetching data from the API: {e}")
        return

    # Initialize the JsonParser service
    parser_service = JsonParser()

    # Parse the league data from the JSON response
    league_data = parser_service.parse_league(json_response)
    teams_and_stats = parser_service.parse_teams_and_stats(json_response)
    teams_data = teams_and_stats['teams']
    team_stats_data = teams_and_stats['team_stats']
    if league_data:
        print("League Data:")
        print(league_data)
        # print("teams_data Data:")
        # print(teams_data)
        # print("team_stats_data Data:")
        # print(team_stats_data)
    else:
        print("Error: League data not found in the response.")

    # Parse games data
    try:
        games = []

        for schedule_date in range(1, 2):  # Looping through calendar dates
            endpoint = f"{base_api_url}72_224_3_{schedule_date}?support_b=false"
            response = api_client.get(endpoint)
            games.extend(parser_service.parse_games(response))  # Parse games for each date

        print("Parsed Games:")
        for game in games:
            print(game)

    except Exception as e:
        print(f"Error fetching or parsing games: {e}")


if __name__ == "__main__":
    main()


import os
from dotenv import load_dotenv
from api_client import APIClient
from json_parser import JsonParser

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Initialize the API client with the API URL
    api_client = APIClient()
    parser_service = JsonParser()


if __name__ == "__main__":
    main()