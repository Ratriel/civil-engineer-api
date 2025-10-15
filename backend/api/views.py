"""
API Views for the Civil Engineer project.

This module contains test endpoints to verify API functionality and logging.
"""

import logging
from django.http import JsonResponse

# ------------------------------------------------------------------------
# Configure logger for this module
# ------------------------------------------------------------------------
logger = logging.getLogger("api")

# ------------------------------------------------------------------------
# Test endpoint
# ------------------------------------------------------------------------
def test_endpoint(request, *args, **kwargs):
    """
    Test API endpoint.

    This endpoint is used to verify that the API is running correctly.
    It logs access and returns a simple JSON response for testing purposes.

    Example request:
        GET /api/test/

    Response:
        {
            "status": "success",
            "message": "API is working correctly."
        }
    """
    # Log access to the test endpoint
    logger.info("Test endpoint called.")

    # Return a basic JSON response
    return JsonResponse({
        "status": "success",
        "message": "API is working correctly."
    })
