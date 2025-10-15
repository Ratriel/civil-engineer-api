"""
URL configuration for the Earthquakes app.

Maps endpoints to corresponding API views.
"""

from django.urls import path
from .views import (
    EarthquakeByStateView,
    EarthquakeByRadiusView,
    RecentAutomaticView,
    RecentFeltView,
    HistoricalView,
)

urlpatterns = [
    # Earthquake retrieval endpoints
    path("us/<str:state_name>/", EarthquakeByStateView.as_view(), name="earthquakes-by-state"),
    path("by-radius/", EarthquakeByRadiusView.as_view(), name="earthquakes-by-radius"),

    # Data storage endpoints for AI usage
    path("recent-automatic/", RecentAutomaticView.as_view(), name="recent-automatic"),
    path("recent-felt/", RecentFeltView.as_view(), name="recent-felt"),
    path("historical/", HistoricalView.as_view(), name="historical"),
]
