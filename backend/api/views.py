import json
from django.http import JsonResponse

# Create your views here.
def home(request, *args, **kwargs):
    print(request.GET.get('abc'))  # Log the HTTP method
    return JsonResponse({"message": "Hello, world!"})