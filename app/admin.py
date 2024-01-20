from django.contrib import admin

# Register your models here.
from app.models.tree_donation_transaction import TreeDonationTransaction, TreeAcceptTransaction, TreeDonationStatus

admin.site.register(TreeDonationTransaction)
admin.site.register(TreeAcceptTransaction)
admin.site.register(TreeDonationStatus)