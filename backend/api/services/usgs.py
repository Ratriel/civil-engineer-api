# backend/api/services/usgs.py
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
