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
    path('user_select_mobile/', views.user_select_mobile, name="user_select_mobile"),
    path('loader/', views.loader, name="loader"),
    path('print_option/', views.print_option, name="print_option"),
    path('mobile_upload/', views.mobile_upload, name="mobile_upload"),
    path('print_preview/<color_mode>/',views.print_preview, name="print_preview"),
    path('print_pay/', views.print_pay, name="print_pay"),
    path('loader_convert_docx/', views.loader_convert_docx,name="loader_convert_docx"),
    path('success_mobile/', views.success_mobile, name="success_mobile"),
    path('logout_admin/', views.logout_admin, name="logout_admin"),
    path('user_select_update_mobile/', views.user_select_update_mobile, name="user_select_update_mobile"),
    path('choose_mode/', views.choose_mode, name="choose_mode"),
    path('confirm_file/', views.confirm_file, name="confirm_file"),
    path('user_select_usb/', views.user_select_usb, name="user_select_usb"),
    
    path('change-html/', views.change_html, name='change-html'),
    path('my-template/', views.my_view, name='my_template'),

]
