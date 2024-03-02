from rest_framework import serializers
from .models import Notification, About

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'timestamp', 'updated_at', 'is_read']



class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
