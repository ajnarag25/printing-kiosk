from re import template
from django.urls import path
# from .views import PasswordsChangeView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="home"),
    path('home_user/', views.home_user, name="home_user"),
    path('home_admin/', views.home_admin, name="home_admin"),
    path('login_admin/', views.login_admin, name="login_admin"),
    path('user_print/', views.user_print, name="user_print"),
    path('user_select/', views.user_select, name="user_select"),
    # path('convert_file/', views.convert_api, name="convert_api")
]

