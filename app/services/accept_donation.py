from app.models.tree_donation_transaction import TreeAcceptTransaction, TreeDonationTransaction
from rest_framework import status

from app.serializers.accept_donation_serializer import AcceptDonationTransactionSerializer

def accept_donation_service(user, data):
    try:
        # Extract the farmer from the user
        farmer = user.Farmer

        # Extract the tree_trans_id and status from the data
        tree_trans_id = data.get('tree_trans_id')
        transaction_status = data.get('status')  # renamed from status to transaction_status

        # Check if the transaction exists and has not been accepted yet
        tree_donation_transaction = TreeDonationTransaction.objects.get(id=tree_trans_id, status="false")
        
        # Create a new TreeAcceptTransaction
        tree_accept_transaction = TreeAcceptTransaction.objects.create(
            tree_trans_id=tree_donation_transaction,
            farmer_id=farmer,
            status=transaction_status  # use transaction_status here
        )
        
        # Update the status of the TreeDonationTransaction
        tree_donation_transaction.status = "true"
        tree_donation_transaction.save()

        # Serialize the TreeAcceptTransaction
        serializer = AcceptDonationTransactionSerializer(tree_accept_transaction)
        
        return serializer.data, status.HTTP_201_CREATED
    except TreeDonationTransaction.DoesNotExist:
        return {"error": "Transaction does not exist or has already been accepted"}, status.HTTP_400_BAD_REQUEST