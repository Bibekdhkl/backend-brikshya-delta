from rest_framework import serializers

from user.models.user import Donors

class DonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donors
        fields = ['id','user', 'donation_balance']
