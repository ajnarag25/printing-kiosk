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
    path('loader/', views.loader, name="loader"),
    path('print_option/', views.print_option, name="print_option"),
    path('mobile_upload/',views.mobile_upload, name="mobile_upload"),
    path('print_preview/<color_mode>/',views.print_preview, name="print_preview"),
    path('print_pay/', views.print_pay, name="print_pay"),
    path('loader_convert_docx/', views.loader_convert_docx,name="loader_convert_docx"),

    path('logout_admin/', views.logout_admin, name="logout_admin"),
]
