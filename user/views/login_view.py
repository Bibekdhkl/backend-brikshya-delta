from rest_framework.response import Response
from rest_framework.decorators import api_view

from user.services.login_service import login_service


@api_view(['POST'])
def login_view(request):
    data,status_code = login_service(request.data)
    return Response(data,status=status_code)