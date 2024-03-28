from django.urls import path
from . import views

urlpatterns = [
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('register/', views.register, name='register'),
    path('login/', views.login),
    path('main/', views.main, name='main'),
    path('', views.login),
]
