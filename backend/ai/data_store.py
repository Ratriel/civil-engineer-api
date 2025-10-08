# backend/ai/data_store.py
import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "earthquake_data.json"

def save_data(endpoint_name: str, data):
    """Guarda los datos recibidos de cada endpoint en un archivo JSON."""
    all_data = load_data()
    all_data[endpoint_name] = data
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

def load_data():
    """Carga los datos almacenados."""
    if not DATA_PATH.exists():
        return {}
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
