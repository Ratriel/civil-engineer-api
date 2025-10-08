from django.urls import path
from .views import CivilEngineeringAgentView

urlpatterns = [
    path('civil-agent/', CivilEngineeringAgentView.as_view(), name='civil-agent'),
]