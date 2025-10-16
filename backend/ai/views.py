"""
AI app views for Civil Engineer API.

This module provides endpoints to:
- Ask questions to the Civil Engineering AI agent
- Generate a dynamic HTML portfolio

Logging is integrated to track requests, responses, and errors.
"""

import random
import logging
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ai.agent import civil_engineering_agent
from ai.portfolio_agent import THEME_DATA, generate_portfolio_html
from django.http import HttpResponse, Http404

# ------------------------------------------------------------------------
# Logger configuration for this module
# ------------------------------------------------------------------------
logger = logging.getLogger("ai")

# ------------------------------------------------------------------------
# Endpoint: Civil Engineering Agent
# ------------------------------------------------------------------------
class CivilEngineeringAgentView(APIView):
    """
    Endpoint to ask questions to the Civil Engineering AI agent.

    POST data:
        question: string, the question to ask the agent

    Response:
        {
            "answer": "AI generated answer"
        }
    """

    def post(self, request):
        question = request.data.get("question")

        if not question:
            logger.warning("No 'question' field in POST data")
            return Response(
                {"error": "You must provide a 'question' field in the body."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        logger.info(f"Received question for AI agent: {question}")

        try:
            answer = civil_engineering_agent(question)
            logger.info("AI agent returned an answer successfully")
            return Response({"answer": answer}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception("Error while querying CivilEngineeringAgent")
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

# ------------------------------------------------------------------------
# Endpoint: Generate Portfolio
# ------------------------------------------------------------------------
def generate_portfolio_view(request):
    """
    Generate a dynamic HTML portfolio based on a random theme.

    Returns a complete HTML document using TailwindCSS and profile data.
    Logs selection and errors for debugging and production monitoring.
    """

    try:
        # Select a random theme
        selected_theme_data = random.choice(THEME_DATA)
        logger.info(f"Selected theme for portfolio: {selected_theme_data.get('Name', 'unknown')}")

        # Generate HTML content
        html_content = generate_portfolio_html(theme_data=selected_theme_data)
        logger.info("Portfolio HTML generated successfully")

        return HttpResponse(
            html_content,
            content_type="text/html; charset=utf-8"
        )
    except Exception as e:
        logger.exception("Error generating portfolio HTML")
        return HttpResponse(
            f"<h2>Error generating portfolio:</h2><pre>{str(e)}</pre>",
            status=500,
            content_type="text/html; charset=utf-8"
        )

# ------------------------------------------------------------------------
# --- View para retornar un CV específico (e.g., /api/cv/1/) ---
def cv_view(request, cv_id):
    """
    Retorna el archivo HTML del CV basado en el ID proporcionado.
    Espera un cv_id como '1', '2', '3', '4'.
    """
    
    # Construir el nombre del archivo (e.g., 'cv1.html')
    cv_filename = f'cv{cv_id}.html'
    
    try:
        # Usa 'render' si 'backend/ai' está configurado como un directorio de templates,
        # lo cual es común en Django para apps pequeñas o si está configurado para buscar templates aquí.
        # Si NO está configurado como directorio de templates, necesitarás leer el archivo manualmente.
        
        # --- Opción 1: Usando `render` (Si 'backend/ai' es un directorio de templates) ---
        # return render(request, cv_filename)
        
        # --- Opción 2: Leyendo el archivo manualmente (Más seguro si no es un directorio de templates) ---
        import os
        from django.conf import settings
        
        # Obtener la ruta absoluta del archivo
        # Asumo que esta vista está en la misma carpeta que los archivos HTML.
        # __file__ es la ruta de este archivo (views.py)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, cv_filename)
        
        if not os.path.exists(file_path):
            raise Http404(f"CV con ID {cv_id} no encontrado.")
            
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        return HttpResponse(html_content, content_type='text/html')
        
    except FileNotFoundError:
        # Esto es solo para la Opción 1 si falla la configuración, pero la Opción 2 lo maneja con `Http404`.
        raise Http404(f"CV con ID {cv_id} no encontrado.")
        
# ------------------------------------------------------------------