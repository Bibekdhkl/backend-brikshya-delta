from django.contrib.auth import authenticate
from rest_framework import status
from user.serializers.login_serializer import LoginSerializers
from user.services.helper.get_token import get_token_for_user 


def login_service(data):
    serializer = LoginSerializers(data=data)
    if serializer.is_valid():
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_token_for_user(user)
            return {"token":token},status.HTTP_200_OK
        
        return {"message":"Invalid credentials"},status.HTTP_401_UNAUTHORIZED
    
    return serializer.errors,status.HTTP_400_BAD_REQUEST