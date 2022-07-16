from django.urls import path



from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/about', views.dashboard_about, name='dashboard_about'),
    # path('dashboard/article', views.dashboar_article, name='dashboard_article'),
    path('dashboard/certificate', views.dashboard_sertificate, name='dashboard_certificate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('documents/', views.documents, name='documents'),
    path('help-handbook/', views.help_handbook, name='help_handbook'),
    path("help_security/", views.help_security_view, name='help_security'),
    path("help_terms/", views.help_terms_view, name='help_terms'),
    path("help/", views.help_view, name='help'),
    # path('media/', views.media_view, name='media'),
    # path('poisk/', views.poisk_view, name='poisk'),
    path('search/', views.search_view, name='search_page'),
 
    # path('test/', views.test_view, name='test'),
    # path('video_error/', views.videos_error_view, name='video_error'),
    # path("videos/", views.videos_view, name='videos'),    
    
    # path('test_quiz/<int:pk>', views.test_quiz_view, name="test_quiz")
]
