from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', register, name="register"),
    # path('login/', user_login, name="login"),
    path('login/', UserLogin.as_view(), name="login"),
    path('profile_dashboard/', profile, name="profile"),
    path('logout/', user_logout, name="logout"),
    # path('logout/', LogoutView.as_view(), name="logout"),
    path('update/', change_user_data, name="update"),
    path('update_password/', update_password, name="password"),
]
