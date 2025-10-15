"""
URL configuration for the API app.

This file maps endpoints to their corresponding view functions.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Basic test endpoint
    path('test/', views.test_endpoint, name='test_endpoint')
]
