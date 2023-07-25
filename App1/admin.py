from django.contrib import admin
# admin.py

from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')  # Display these fields in the admin list view
    search_fields = ('name',)      # Add fields you want to search by in the admin
    # Add any other configurations you want for the admin interface

# Register your models here.
