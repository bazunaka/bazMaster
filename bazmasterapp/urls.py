from django.urls import path
from . import views

urlpatterns = [
    path('forgot-password', views.forgot_password),
    path('register/', views.register),
    path('login/', views.login),
    path('main/', views.main),
    path('', views.login),
]
