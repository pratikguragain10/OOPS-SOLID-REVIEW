import csv
from .BaseExporter import BaseExporter

class CSVExporter(BaseExporter):
    def export(self, data, filename):
        if not data:
            print(f"No data to export to {filename}")
            return
        keys = data[0].keys()
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data exported to {filename}")
