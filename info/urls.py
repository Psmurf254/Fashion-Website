from django.urls import path
from . import views
from .views import NotificationList, NotificationDetail
from .views import  create_notification

urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/createNotification/', create_notification, name='create_notification'),
    path('notifications/<int:pk>/', NotificationDetail.as_view(), name='notification-detail'),
    path('about/', views.getAbout, name='about'),
]
