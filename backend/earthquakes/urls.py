"""
URL configuration for the Earthquakes app.

Maps endpoints to corresponding API views.
"""

from django.urls import path
from .views import (
    EarthquakeByStateView,
    EarthquakeByRadiusView,
    GetHistoricalView,      # <- Vista para obtener data histórica
    GetRecentAutomaticView,
    GetRecentFeltView,
    RecentAutomaticView,
    RecentFeltView,
    HistoricalView,
)

urlpatterns = [
    # -----------------------------------------------
    # 1. Earthquake retrieval endpoints (Existing)
    # -----------------------------------------------
    path("us/<str:state_name>/", EarthquakeByStateView.as_view(), name="earthquakes-by-state"),
    path("by-radius/", EarthquakeByRadiusView.as_view(), name="earthquakes-by-radius"),

    # -----------------------------------------------
    # 2. Data storage endpoints for AI usage (POST)
    # -----------------------------------------------
    path("recent-automatic/", RecentAutomaticView.as_view(), name="recent-automatic"),
    path("recent-felt/", RecentFeltView.as_view(), name="recent-felt"),
    path("historical/", HistoricalView.as_view(), name="historical"), # Endpoint de almacenamiento (POST)

    # -----------------------------------------------
    # 3. Data retrieval endpoints for AI usage (GET)
    # -----------------------------------------------
    path('get/automatic/', GetRecentAutomaticView.as_view(), name='get-automatic'),
    path('get/felt/', GetRecentFeltView.as_view(), name='get-felt'),
    
    # NUEVO: Endpoint para obtener data histórica (GET)
    path('get/historical/', GetHistoricalView.as_view(), name='get-historical'), 
]