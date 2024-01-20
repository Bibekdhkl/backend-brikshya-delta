from rest_framework import serializers  
from user.models.user import User

class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(max_length = 255, min_length =6, write_only=True)
    class Meta:
        model = User 
        fields = ["email","password","phone","password2","name","role"]
        extra_kwargs = {
            'password': {'write_only': True},
        }
        
    def validate(self,data):
        password = data.get('password')
        password2 = data.get('password2')
        if password != password2:
            raise serializers.ValidationError("Passwords must match")
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)