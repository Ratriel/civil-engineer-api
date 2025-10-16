"""
URL configuration for the AI app.

Maps endpoints to Civil Engineering AI agent and portfolio generator.
"""

from django.urls import path
from .views import CivilEngineeringAgentView, generate_portfolio_view, cv_view

urlpatterns = [
    # AI agent endpoint (POST)
    path('civil-agent/', CivilEngineeringAgentView.as_view(), name='civil-agent'),

    # Dynamic portfolio generator (GET)
    path('generate-portfolio/', generate_portfolio_view, name='generate_portfolio'),
    path('cv/<int:cv_id>/', cv_view, name='cv_view'),  # e.g., /api/cv/1/
]
