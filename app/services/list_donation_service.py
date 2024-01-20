from rest_framework import status
from app.models.tree_donation_transaction import TreeDonationTransaction
from app.serializers.make_donation_serializer import TreeDonationTransactionSerializer
from user.models.user import Donors

def list_donation_service(user):
    # Get the Donors instance associated with the user
    donor = Donors.objects.get(user=user)

    # Filter the donations with status="true"
    donations = TreeDonationTransaction.objects.filter(donar_id=donor)

    # Serialize the donations
    serializer = TreeDonationTransactionSerializer(donations, many=True)

    return serializer.data, status.HTTP_200_OK