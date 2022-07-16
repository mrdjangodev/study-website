from django.urls import path
from  . import views


urlpatterns = [
    path('inner/<str:type>/', views.store_inner_view, name='resources-inner'),
    path('main/', views.store_view, name='resources-main'),
    path('download/<int:pk>/', views.download_file, name='download-file'),
]
