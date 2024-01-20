from rest_framework import serializers
from user.models import User

class LoginSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    class Meta:
        model = User
        fields = ["email","password"]
