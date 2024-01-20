from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from user.services.register_service import register_service


@api_view(['POST'])
def register_view(request):
    data, status_code = register_service(request.data)
    return Response(data, status=status_code)