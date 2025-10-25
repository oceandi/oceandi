# constants.py
import json
from pathlib import Path

class Constants:
    """Evrensel sabitlerin JSON dosyasından okunması için basit bir sınıf."""
    def __init__(self, filepath="constants.json"):
        with open(Path(filepath), "r", encoding="utf-8") as f:
            self._data = json.load(f)

    def get(self, category, name):
        """Bir sabiti kategori ve isimle getir."""
        return self._data.get(category, {}).get(name)

    def __getitem__(self, key):
        """Alternatif kısayol: CONST['mathematical_constants.pi']"""
        category, const_name = key.split(".")
        return self._data[category][const_name]

# Kullanım örneği:
if __name__ == "__main__":
    CONST = Constants()
    print("Işık hızı:", CONST["fundamental_constants.speed_of_light_c"])
    print("Altın oran (phi):", CONST["mathematical_constants.phi"])
