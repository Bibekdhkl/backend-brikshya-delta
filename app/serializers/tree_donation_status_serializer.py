from rest_framework import serializers

from app.models.tree_donation_transaction import TreeDonationStatus

class TreeDonationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreeDonationStatus
        fields = ["id", "tree_accept_id", "status", "comments", "image_path", "created_at"]