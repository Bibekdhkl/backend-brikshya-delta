from rest_framework import serializers
from app.models.tree_donation_transaction import TreeDonationTransaction, TreeAcceptTransaction, TreeDonationStatus
from app.serializers.accept_donation_serializer import AcceptDonationTransactionSerializer

class TreeDonationTransactionSerializer(serializers.ModelSerializer):
    donation_amount = serializers.IntegerField(required=False)
    tree_donation_status_status = serializers.SerializerMethodField()
    tree_donation_status_comments = serializers.SerializerMethodField()
    tree_donation_status_image_path = serializers.SerializerMethodField()

    class Meta:
        model = TreeDonationTransaction
        fields = ["id", "donation_name", "donation_description","tree_count", "donation_amount", "status", "created_at","donar_id", "tree_donation_status_status", "tree_donation_status_comments", "tree_donation_status_image_path"]

    def get_tree_donation_status_status(self, obj):
        try:
            accept_transaction = TreeAcceptTransaction.objects.get(tree_trans_id=obj)
            donation_status = TreeDonationStatus.objects.get(tree_accept_id=accept_transaction.id)
            return donation_status.status
        except (TreeAcceptTransaction.DoesNotExist, TreeDonationStatus.DoesNotExist):
            return None

    def get_tree_donation_status_comments(self, obj):
        try:
            accept_transaction = TreeAcceptTransaction.objects.get(tree_trans_id=obj)
            donation_status = TreeDonationStatus.objects.get(tree_accept_id=accept_transaction.id)
            return donation_status.comments
        except (TreeAcceptTransaction.DoesNotExist, TreeDonationStatus.DoesNotExist):
            return None

    def get_tree_donation_status_image_path(self, obj):
        try:
            accept_transaction = TreeAcceptTransaction.objects.get(tree_trans_id=obj)
            donation_status = TreeDonationStatus.objects.get(tree_accept_id=accept_transaction.id)
            if donation_status.image_path and donation_status.image_path.name:
                return donation_status.image_path.url
            else:
                return '/image.jpg'  # replace with your actual default image path
        except (TreeAcceptTransaction.DoesNotExist, TreeDonationStatus.DoesNotExist):
            return '/image.jpg'  # replace with your actual default image path