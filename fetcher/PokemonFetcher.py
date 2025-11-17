import requests

class PokemonFetcher:
    """Fetch pokemon data from the API"""
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self, limit=10):
        self.limit = limit

    def fetch_pokemon_list(self):
        response = requests.get(self.BASE_URL, params={"limit": self.limit})
        response.raise_for_status()
        data = response.json()
        return data["results"]

    def fetch_pokemon_details(self, url):
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        return {"name": data["name"], "abilities": abilities}

