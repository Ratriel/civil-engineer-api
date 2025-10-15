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
        logger.info(f"Selected theme for portfolio: {selected_theme_data.get('name', 'unknown')}")

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
