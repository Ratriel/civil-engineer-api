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
        # Devuelve un diccionario vacío si el archivo no existe para evitar errores.
        return {}
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            # Asumimos que el JSON contiene un diccionario donde las claves son
            # "recent_automatic", "recent_felt", "historical", etc.
            return json.load(f)
    except json.JSONDecodeError:
        return {}