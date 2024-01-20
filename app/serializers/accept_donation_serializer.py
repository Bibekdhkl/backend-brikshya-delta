from rest_framework import serializers
from app.models.tree_donation_transaction import TreeAcceptTransaction, TreeDonationTransaction

class AcceptDonationTransactionSerializer(serializers.ModelSerializer):
    donation_name = serializers.SerializerMethodField()
    donation_description = serializers.SerializerMethodField()
    donation_amount = serializers.SerializerMethodField()
    tree_count = serializers.SerializerMethodField()

    class Meta:
        model = TreeAcceptTransaction
        fields = ["id", "tree_trans_id", "farmer_id", "status", "created_at", "donation_name", "donation_description", "donation_amount", "tree_count"]

    def get_donation_name(self, obj):
        return obj.tree_trans_id.donation_name

    def get_donation_description(self, obj):
        return obj.tree_trans_id.donation_description

    def get_donation_amount(self, obj):
        return obj.tree_trans_id.donation_amount

    def get_tree_count(self, obj):
        return obj.tree_trans_id.tree_count