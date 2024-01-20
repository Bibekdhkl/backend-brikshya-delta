from rest_framework import serializers

from app.models.tree_donation_transaction import TreeDonationTransaction


class TreeDonationTransactionSerializer(serializers.ModelSerializer):
    donation_amount = serializers.IntegerField(required=False)

    class Meta:
        model = TreeDonationTransaction
        fields = ["id", "donation_name", "donation_description","tree_count", "donation_amount", "status", "created_at","donar_id"]