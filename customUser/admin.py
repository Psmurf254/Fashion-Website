

from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'date_of_birth', 'contact_phone', 'contact_email')
    search_fields = ('full_name', 'contact_phone', 'contact_email')
    list_filter = ('gender', 'telemedicine_consultations_allowed')

