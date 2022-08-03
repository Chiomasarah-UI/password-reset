from re import template
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls.static import static
from . import views
from .views import reset
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    
    

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='loginAuth/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='loginAuth/password_change.html'), 
        name='password_change'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='loginAuth/password_reset.html'), name='password_reset'), 

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='loginAuth/password_reset_done.html'),
     name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='loginAuth/password_reset_confirm.html' ), 
        name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='loginAuth/password_reset_complete.html'),
     name='password_reset_complete'),
    
]
