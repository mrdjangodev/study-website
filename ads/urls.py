from django.urls import path
from . import views
urlpatterns = [
    path('notification/', views.notification_view, name='notification'),
    path('mark_read_all/', views.mark_read_all, name='mark_read_all'),
]
