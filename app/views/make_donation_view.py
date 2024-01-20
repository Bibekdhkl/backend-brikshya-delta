from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from app.services.list_donation_service import list_donation_service

from app.services.make_donation_service import make_donation_service

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_donation_view(request):
    data, status_code = make_donation_service(request.user, request.data)
    return Response(data, status=status_code)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_donation_view(request):
    data, status_code = list_donation_service(request.user)
    return Response(data, status=status_code)

