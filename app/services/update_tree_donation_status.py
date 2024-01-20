from rest_framework import status
from app.models.tree_donation_transaction import TreeDonationStatus, TreeAcceptTransaction
from app.serializers.tree_donation_status_serializer import TreeDonationStatusSerializer

from django.http import Http404


def update_tree_donation_status_service(user, data, tree_donation_status_id):
    # Get the TreeDonationStatus instance with the given id
    try:
        tree_donation_status = TreeDonationStatus.objects.get(id=tree_donation_status_id)
    except TreeDonationStatus.DoesNotExist:
        raise Http404("TreeDonationStatus with the given id does not exist")

    # Check if the user is a farmer
    if not user.Farmer:
        return {"error": "You are not authorized to update this TreeDonationStatus. Only farmers can update this."}, status.HTTP_403_FORBIDDEN

    # Check if the user is the one who accepted the donation
    # tree_accept_transaction = tree_donation_status.tree_accept_id
    # if tree_accept_transaction.farmer_id != user:
    #     return {"error": "You are not authorized to update this TreeDonationStatus. Only the farmer who accepted the donation can update this."}, status.HTTP_403_FORBIDDEN

    # Update the TreeDonationStatus instance with the data
    serializer = TreeDonationStatusSerializer(tree_donation_status, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return serializer.data, status.HTTP_200_OK
    else:
        return serializer.errors, status.HTTP_400_BAD_REQUEST