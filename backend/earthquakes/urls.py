# backend/earthquakes/urls.py
from django.urls import path
from .views import (
    EarthquakeByStateView,
    EarthquakeByRadiusView,
    RecentAutomaticView,
    RecentFeltView,
    HistoricalView,
)

urlpatterns = [
    path("us/<str:state_name>/", EarthquakeByStateView.as_view(), name="earthquakes-by-state"),

    # nuevos endpoints para recibir datos
    path("by-radius/", EarthquakeByRadiusView.as_view(), name="by-radius"),  # 👈 nuevo
    path("recent-automatic/", RecentAutomaticView.as_view(), name="recent-automatic"),
    path("recent-felt/", RecentFeltView.as_view(), name="recent-felt"),
    path("historical/", HistoricalView.as_view(), name="historical"),
]
