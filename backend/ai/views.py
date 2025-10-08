# backend/ai/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ai.agent import civil_engineering_agent

class CivilEngineeringAgentView(APIView):
    """
    Endpoint para hacer preguntas al agente de ingeniería civil.
    """

    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "Debe enviar 'question' en el body"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            answer = civil_engineering_agent(question)
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
