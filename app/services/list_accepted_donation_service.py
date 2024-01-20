from app.models.tree_donation_transaction import TreeAcceptTransaction, TreeDonationTransaction
from rest_framework import status

from app.serializers.accept_donation_serializer import AcceptDonationTransactionSerializer

def list_accepted_donation_service(user):
    # Extract the farmer from the user
    farmer = user.Farmer

    # Get all TreeAcceptTransaction instances accepted by the farmer
    accepted_transactions = TreeAcceptTransaction.objects.filter(farmer_id=farmer)

    # Serialize the TreeAcceptTransaction instances
    serializer = AcceptDonationTransactionSerializer(accepted_transactions, many=True)

    return serializer.data, status.HTTP_200_OK