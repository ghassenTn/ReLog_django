# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_client, name='register_client'),
    path('login/', views.custom_login, name='login'),
    # Add other URL patterns as needed
]
