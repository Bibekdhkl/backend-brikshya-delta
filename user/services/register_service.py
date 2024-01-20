from django.contrib.auth import authenticate

from rest_framework import status

from user.serializers.register_serilaizer import RegisterSerializer
from user.services.helper.get_token import get_token_for_user

def register_service(data):
    serializer = RegisterSerializer(data=data)
    
    if serializer.is_valid():
        user = serializer.save()
        token = get_token_for_user(user)
        response_data = serializer.data
        response_data['token'] = token
        return response_data, status.HTTP_201_CREATED
    return serializer.errors, status.HTTP_400_BAD_REQUEST