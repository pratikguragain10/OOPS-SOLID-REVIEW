from .BaseExporter import BaseExporter

class TXTExporter(BaseExporter):
    def export(self, data, filename):
        with open(filename, 'w') as f:
            for item in data:
                f.write(f"Name: {item['name']}\nAbilities: {', '.join(item['abilities'])}\n\n")
        print(f"Data exported to {filename}")
