# backend/api/services/usgs.py
from django.http import JsonResponse
from datetime import datetime
import requests
from earthquakes.utils.state_bboxes import STATE_BBOXES


USGS_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

def get_earthquakes_by_state(state_name, starttime, endtime):
    state_name = state_name.lower()
    if state_name not in STATE_BBOXES:
        raise ValueError(f"Bounding box not defined for state: {state_name}")
    
    bbox = STATE_BBOXES[state_name]

    params = {
        "format": "geojson",
        "starttime": starttime,
        "endtime": endtime,
        "minlatitude": bbox["min_lat"],
        "maxlatitude": bbox["max_lat"],
        "minlongitude": bbox["min_lon"],
        "maxlongitude": bbox["max_lon"],
    }
    response = requests.get(USGS_URL, params=params)
    return response.json()


def get_earthquakes_by_radius(latitude, longitude, maxradiuskm, starttime, endtime):
    """
    Obtiene sismos desde la API USGS dentro de un radio (en km) desde una coordenada.
    """
    params = {
        "format": "geojson",
        "starttime": starttime,
        "endtime": endtime,
        "latitude": latitude,
        "longitude": longitude,
        "maxradiuskm": maxradiuskm,
    }

    response = requests.get(USGS_URL, params=params)
    response.raise_for_status()
    return response.json()