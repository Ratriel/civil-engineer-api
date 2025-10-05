# backend/earthquakes/urls.py
from django.urls import path
from .views import (
    EarthquakeByStateView,
    RecentAutomaticView,
    RecentFeltView,
    HistoricalView,
)

urlpatterns = [
    path("us/<str:state_name>/", EarthquakeByStateView.as_view(), name="earthquakes-by-state"),

    # nuevos endpoints para recibir datos
    path("recent-automatic/", RecentAutomaticView.as_view(), name="recent-automatic"),
    path("recent-felt/", RecentFeltView.as_view(), name="recent-felt"),
    path("historical/", HistoricalView.as_view(), name="historical"),
]
