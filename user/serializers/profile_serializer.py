from rest_framework import serializers
from user.models.user import User
from user.serializers.donor_serializer import DonorsSerializer

from user.serializers.farmer_serializer import FarmerSerializer

class ProfileSerializer(serializers.ModelSerializer):
    Donors = DonorsSerializer(read_only=True)
    Farmer = FarmerSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "phone","name", "role", "created_at", "Donors", "Farmer"]
        
