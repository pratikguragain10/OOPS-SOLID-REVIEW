from fetcher.PokemonFetcher import PokemonFetcher
from exporters.BaseExporter import BaseExporter

class PokemonManager:
    """Manager class to fetch and export pokemon data"""
    def __init__(self, fetcher: PokemonFetcher, exporters: list[BaseExporter]):
        self.fetcher = fetcher
        self.exporters = exporters

    def run(self):
        pokemon_list = self.fetcher.fetch_pokemon_list()
        detailed_data = [self.fetcher.fetch_pokemon_details(pokemon["url"]) for pokemon in pokemon_list]

        for exporter in self.exporters:
            ext = exporter.__class__.__name__.replace("Exporter", "").lower()
            exporter.export(detailed_data, f"pokemons.{ext}")
