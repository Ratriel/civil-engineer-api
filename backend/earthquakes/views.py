# backend/earthquakes/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services.usgs import get_earthquakes_by_radius, get_earthquakes_by_state
from ai.data_store import save_data


class EarthquakeByStateView(APIView):
    def get(self, request, state_name):
        starttime = request.GET.get("starttime", "2025-01-01")
        endtime = request.GET.get("endtime", "2025-12-31")

        try:
            data = get_earthquakes_by_state(state_name, starttime, endtime)
            return Response(data, status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
class EarthquakeByRadiusView(APIView):
    """
    Obtiene eventos sísmicos por coordenadas y radio.
    Ejemplo:
    /earthquakes/by-radius/?lat=34.05&lon=-118.24&radius=100
    """

    def get(self, request):
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")
        radius = request.GET.get("radius", 100)
        starttime = request.GET.get("starttime", "2025-01-01")
        endtime = request.GET.get("endtime", "2025-12-31")

        # Validar entrada
        if not lat or not lon:
            return Response(
                {"error": "Debe enviar lat y lon como parámetros."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            data = get_earthquakes_by_radius(lat, lon, radius, starttime, endtime)
            save_data(f"radius_{lat}_{lon}_{radius}", data)  # 👈 almacena para el agente
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class RecentAutomaticView(APIView):
    def post(self, request):
        data = request.data
        save_data("recent_automatic", data)
        return Response({"message": "Data almacenada"}, status=status.HTTP_201_CREATED)

class RecentFeltView(APIView):
    def post(self, request):
        data = request.data
        save_data("recent_felt", data)
        return Response({"message": "Data almacenada"}, status=status.HTTP_201_CREATED)

class HistoricalView(APIView):
    def post(self, request):
        data = request.data
        save_data("historical", data)
        return Response({"message": "Data almacenada"}, status=status.HTTP_201_CREATED)
