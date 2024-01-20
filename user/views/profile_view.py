from rest_framework.decorators import api_view, permission_classes

from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from user.services.profile_service import profile_edit_service, profile_view_service

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile_get_view(request):
    data, status_code = profile_view_service(request.user)
    return Response(data, status=status_code)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def profile_edit_view(request):
    data, status_code = profile_edit_service(request.user, request.data)
    return Response(data, status=status_code)
