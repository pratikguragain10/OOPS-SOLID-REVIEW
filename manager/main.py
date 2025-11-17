from fetcher.PokemonFetcher import PokemonFetcher
from exporters.CSVExporter import CSVExporter
from exporters.JSONExporter import JSONExporter
from exporters.TXTExporter import TXTExporter
from exporters.PDFExporter import PDFExporter
from manager.PokemonManager import PokemonManager

if __name__ == "__main__":
    fetcher = PokemonFetcher(limit=25)
    exporters = [CSVExporter(), JSONExporter(), TXTExporter(), PDFExporter()]
    manager = PokemonManager(fetcher, exporters)
    manager.run()
