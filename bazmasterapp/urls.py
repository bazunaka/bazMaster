from django.urls import path
from .import views

urlpatterns = [
    path('auth/', views.auth),
    path('main/', views.main),
    path('', views.index),
]