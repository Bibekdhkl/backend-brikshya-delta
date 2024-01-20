from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

from rest_framework.permissions import IsAuthenticated

from app.services.accept_donation import accept_donation_service
from app.services.firebase.readSensors import get_sensor_data
from app.services.list_accepted_donation_service import list_accepted_donation_service
from app.services.list_all_donations import list_all_donation_service
from app.services.update_tree_donation_status import update_tree_donation_status_service

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def accept_donation_view(request):
    data, status_code = accept_donation_service(request.user, request.data)
    return Response(data, status=status_code)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_accepted_donation_view(request):
    data, status_code = list_accepted_donation_service(request.user)
    return Response(data, status=status_code)

@api_view(['GET'])
def get_firebase_data(request):
    data = get_sensor_data()
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_all_donation_view(request):
    data, status_code = list_all_donation_service()
    return Response(data, status=status_code)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_tree_donation_status_view(request, tree_accept_id):
    data, http_status = update_tree_donation_status_service(request.user, request.data, tree_accept_id)
    return Response(data, status=http_status)