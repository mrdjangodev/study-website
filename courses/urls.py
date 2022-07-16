from django.urls import path
from . import views

urlpatterns = [

    path("info/<int:pk>", views.info_view, name='info'), 
    path('lesson_main/<int:pk>', views.lesson_main_view, name='lesson_main'),
    path('lesson_local/<int:course_section_id>/<int:pk>', views.lesson_view, name='local_lesson'),
    
    path("home3/", views.home3_view, name='home3'),
    path('dash_index/', views.dashboard_index_view, name='dashboard_index'),
]
