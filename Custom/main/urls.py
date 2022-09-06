from django.urls import path
from .views import home,register_user,login_user
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('',home,name='home'),
    path('login_user/',login_user,name='login'),
    path('register_user/',register_user,name='register'),
    path("logout/", LogoutView.as_view(), name="logout")
]
