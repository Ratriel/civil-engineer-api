import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ai.agent import civil_engineering_agent
from ai.portfolio_agent import THEME_DATA, generate_portfolio_html
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


def generate_portfolio_view(request):
    """
    Endpoint que genera el portafolio HTML dinámicamente.
    Selecciona un diccionario de tema aleatorio de THEME_DATA.
    """

    try:
        # 1. Selección aleatoria del diccionario de tema completo
        selected_theme_data = random.choice(THEME_DATA)
        
        # 2. Llamada a la función pasándole el diccionario completo
        html_content = generate_portfolio_html(theme_data=selected_theme_data)
        
        # Opcional: Para debugging, puedes añadir el tema seleccionado al inicio del HTML
        # html_content = f"\n" + html_content
        
        return HttpResponse(
            html_content,
            content_type="text/html; charset=utf-8"
        )
    except Exception as e:
        # Manejo de errores
        return HttpResponse(
            f"<h2>Error generando el portafolio:</h2><pre>{str(e)}</pre>",
            status=500,
            content_type="text/html; charset=utf-8"
        )