from rest_framework import status
from app.serializers.make_donation_serializer import TreeDonationTransactionSerializer
from user.models.user import Donors 

def make_donation_service(user, data):
    # Get the Donors instance associated with the user
    donor = Donors.objects.get(user=user)

    # Add the donar_id to the data
    data['donar_id'] = donor.id

    serializer = TreeDonationTransactionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED
    return serializer.errors, status.HTTP_400_BAD_REQUEST