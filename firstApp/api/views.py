from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

@api_view()
@permission_classes([IsAuthenticated])
def firstFunction(request):
    return Response({"message": "We Received Your Request"})