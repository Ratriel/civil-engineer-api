"""
Earthquakes API Views

This module provides endpoints to retrieve earthquake data from USGS
and store it for the AI agent. Logging is added to track requests,
responses, and errors.
"""

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services.usgs import get_earthquakes_by_radius, get_earthquakes_by_state
from ai.data_store import save_data

# ------------------------------------------------------------------------
# Logger configuration for this module
# ------------------------------------------------------------------------
logger = logging.getLogger("earthquakes")

# ------------------------------------------------------------------------
# Endpoint: Get earthquakes by US state
# ------------------------------------------------------------------------
class EarthquakeByStateView(APIView):
    """
    Retrieve earthquake events by US state within a date range.

    GET parameters:
        starttime: optional, default "2025-01-01"
        endtime: optional, default "2025-12-31"

    Example:
        /earthquakes/us/California/?starttime=2025-01-01&endtime=2025-12-31
    """

    def get(self, request, state_name):
        starttime = request.GET.get("starttime", "2025-01-01")
        endtime = request.GET.get("endtime", "2025-12-31")

        logger.info(f"Request for earthquakes in state={state_name}, start={starttime}, end={endtime}")

        try:
            data = get_earthquakes_by_state(state_name, starttime, endtime)
            logger.info(f"Retrieved {len(data)} earthquake events for state {state_name}")
            return Response(data, status=status.HTTP_200_OK)
        except ValueError as e:
            logger.warning(f"Validation error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("Unexpected error in EarthquakeByStateView")
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ------------------------------------------------------------------------
# Endpoint: Get earthquakes by coordinates and radius
# ------------------------------------------------------------------------
class EarthquakeByRadiusView(APIView):
    """
    Retrieve earthquake events by latitude, longitude, and radius.

    GET parameters:
        lat: latitude (required)
        lon: longitude (required)
        radius: in km, optional, default 100
        starttime: optional, default "2025-01-01"
        endtime: optional, default "2025-12-31"

    Example:
        /earthquakes/by-radius/?lat=34.05&lon=-118.24&radius=100
    """

    def get(self, request):
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        radius = request.GET.get("radius", 100)
        starttime = request.GET.get("starttime", "2025-01-01")
        endtime = request.GET.get("endtime", "2025-12-31")

        if not lat or not lon:
            logger.warning("Missing latitude or longitude parameters")
            return Response(
                {"error": "lat and lon parameters are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        logger.info(f"Request for earthquakes by radius: lat={lat}, lon={lon}, radius={radius}")

        try:
            data = get_earthquakes_by_radius(lat, lon, radius, starttime, endtime)
            save_data(f"radius_{lat}_{lon}_{radius}", data)
            logger.info(f"Retrieved {len(data)} earthquake events for radius query")
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("Unexpected error in EarthquakeByRadiusView")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ------------------------------------------------------------------------
# Endpoint: Store recent automatic earthquakes
# ------------------------------------------------------------------------
class RecentAutomaticView(APIView):
    """
    Store recent automatic earthquake data for AI usage.

    POST data:
        JSON payload containing earthquake information.

    Response:
        {"message": "Data stored"}
    """

    def post(self, request):
        data = request.data
        logger.info(f"Storing recent automatic earthquake data, {len(data)} records")
        save_data("recent_automatic", data)
        return Response({"message": "Data stored"}, status=status.HTTP_201_CREATED)

# ------------------------------------------------------------------------
# Endpoint: Store recent felt earthquakes
# ------------------------------------------------------------------------
class RecentFeltView(APIView):
    """
    Store recent felt earthquake data for AI usage.

    POST data:
        JSON payload containing earthquake information.
    """

    def post(self, request):
        data = request.data
        logger.info(f"Storing recent felt earthquake data, {len(data)} records")
        save_data("recent_felt", data)
        return Response({"message": "Data stored"}, status=status.HTTP_201_CREATED)

# ------------------------------------------------------------------------
# Endpoint: Store historical earthquakes
# ------------------------------------------------------------------------
class HistoricalView(APIView):
    """
    Store historical earthquake data for AI usage.

    POST data:
        JSON payload containing earthquake information.
    """

    def post(self, request):
        data = request.data
        logger.info(f"Storing historical earthquake data, {len(data)} records")
        save_data("historical", data)
        return Response({"message": "Data stored"}, status=status.HTTP_201_CREATED)
