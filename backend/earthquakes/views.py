# backend/earthquakes/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.services.usgs import get_earthquakes_by_state

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


class RecentAutomaticView(APIView):
    def post(self, request):
        print("Data recibida en /earthquakes/recent-earthquakes/automatic/")
        print(request.data)  # imprime el JSON recibido
        return Response({"message": "Data recibida"}, status=status.HTTP_201_CREATED)


class RecentFeltView(APIView):
    def post(self, request):
        print("Data recibida en /earthquakes/recent-felt/")
        print(request.data)
        return Response({"message": "Data recibida"}, status=status.HTTP_201_CREATED)


class HistoricalView(APIView):
    def post(self, request):
        print("Data recibida en /earthquakes/historical/")
        print(request.data)
        return Response({"message": "Data recibida"}, status=status.HTTP_201_CREATED)