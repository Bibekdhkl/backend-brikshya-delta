from rest_framework import status

from user.serializers.profile_serializer import ProfileSerializer 


def profile_view_service(user):
    serializer = ProfileSerializer(user)
    return serializer.data, status.HTTP_200_OK

def profile_edit_service(user,data):
    serializer = ProfileSerializer(user,data=data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_200_OK
    
    return serializer.errors, status.HTTP_400_BAD_REQUEST