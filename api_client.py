import requests

class APIClient:
    def get(self, base_url):
        """
        Makes a GET request to the API and returns the response.
        """
        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                return response.json()  # Assuming the API returns JSON data
            else:
                raise Exception(f"Failed to retrieve data: {response.status_code}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"An error occurred while making the API call: {e}")
