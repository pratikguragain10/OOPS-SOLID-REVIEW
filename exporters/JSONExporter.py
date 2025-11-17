import json
from .BaseExporter import BaseExporter

class JSONExporter(BaseExporter):
    def export(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data exported to {filename}")
