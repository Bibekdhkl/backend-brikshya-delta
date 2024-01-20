from django.urls import path
from app.views.accept_donation_view import accept_donation_view, get_firebase_data, list_accepted_donation_view, list_all_donation_view, update_tree_donation_status_view

from app.views.make_donation_view import list_donation_view, make_donation_view
urlpatterns = [
    path('donate/', make_donation_view, name="make-donation"),
    path('donations/', list_donation_view, name="list-donations"),
    path('accept-donation/',accept_donation_view, name="accept-donation"),
    path('list-accept-donation/',list_accepted_donation_view,name="list-accept-donation"),
    path('update-tree-donation-status/<int:tree_accept_id>/', update_tree_donation_status_view, name="update-tree-donation-status"),
    path('list-all-donation/', list_all_donation_view, name="list-all-donation"),
    path('get-firebase-data/', get_firebase_data, name='get-firebase-data')
]