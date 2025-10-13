from django.urls import path
from .views import CivilEngineeringAgentView, generate_portfolio_view

urlpatterns = [
    path('civil-agent/', CivilEngineeringAgentView.as_view(), name='civil-agent'),
    path("generate-portfolio/", generate_portfolio_view, name="generate_portfolio"),
]