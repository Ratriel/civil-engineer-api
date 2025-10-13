from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ai.agent import civil_engineering_agent
from ai.portfolio_agent import generate_portfolio_html
from django.http import HttpResponse


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


# 👇 Nuevo endpoint separado y visible para importar desde urls.py
def generate_portfolio_view(request):
    """
    Endpoint que genera el portafolio HTML dinámicamente
    basado en el estilo pasado por parámetro (?estilo=dark, etc.)
    """
    style = request.GET.get("estilo", "dark")
    try:
        html_content = generate_portfolio_html(style)
        return HttpResponse(
            html_content,
            content_type="text/html; charset=utf-8"
        )
    except Exception as e:
        return HttpResponse(
            f"<h2>Error generando el portafolio:</h2><pre>{str(e)}</pre>",
            status=500,
            content_type="text/html; charset=utf-8"
        )
