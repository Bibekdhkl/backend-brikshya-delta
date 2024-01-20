from rest_framework import serializers
from app.models.tree_donation_transaction import TreeAcceptTransaction, TreeDonationTransaction, TreeDonationStatus

class AcceptDonationTransactionSerializer(serializers.ModelSerializer):
    donation_name = serializers.SerializerMethodField()
    donation_description = serializers.SerializerMethodField()
    donation_amount = serializers.SerializerMethodField()
    tree_count = serializers.SerializerMethodField()
    tree_donation_status_id = serializers.SerializerMethodField()
    tree_donation_status_status = serializers.SerializerMethodField()
    tree_donation_status_comments = serializers.SerializerMethodField()
    tree_donation_status_image_path = serializers.SerializerMethodField()

    class Meta:
        model = TreeAcceptTransaction
        fields = ["id", "tree_trans_id", "farmer_id", "status", "created_at", "donation_name", "donation_description", "donation_amount", "tree_count", "tree_donation_status_id", "tree_donation_status_status", "tree_donation_status_comments", "tree_donation_status_image_path"]

    def get_donation_name(self, obj):
        return obj.tree_trans_id.donation_name

    def get_donation_description(self, obj):
        return obj.tree_trans_id.donation_description

    def get_donation_amount(self, obj):
        return obj.tree_trans_id.donation_amount

    def get_tree_count(self, obj):
        return obj.tree_trans_id.tree_count

    def get_tree_donation_status_id(self, obj):
        return TreeDonationStatus.objects.get(tree_accept_id=obj.id).id

    def get_tree_donation_status_status(self, obj):
        return TreeDonationStatus.objects.get(tree_accept_id=obj.id).status

    def get_tree_donation_status_comments(self, obj):
        return TreeDonationStatus.objects.get(tree_accept_id=obj.id).comments

    def get_tree_donation_status_image_path(self, obj):
        try:
            tree_donation_status = TreeDonationStatus.objects.get(tree_accept_id=obj.id)
            if tree_donation_status.image_path and tree_donation_status.image_path.name:
                return tree_donation_status.image_path.url
            else:
                return '/image.jpg'  # replace with your actual default image path
        except TreeDonationStatus.DoesNotExist:
            return '/image.jpg'  # replace with your actual default image path