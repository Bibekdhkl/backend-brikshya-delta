from rest_framework import serializers
from user.models import Donors, Farmer


class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id','user', 'latitude', 'interest', 'wallet_amount']