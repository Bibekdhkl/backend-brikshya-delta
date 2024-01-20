from django.urls import path
from user.views.register_view import register_view
from user.views.login_view import login_view
from user.views.profile_view import profile_edit_view, profile_get_view
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/',register_view,name="register" ),
    path('login/',login_view,name="login" ),
    path('profile/',profile_get_view,name="profile" ),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/edit/',profile_edit_view,name="profile-edit" ),
]