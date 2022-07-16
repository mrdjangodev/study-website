from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('default_register_login_page/', views.register_login_page, name='register_login_page'),
    path('register/<str:data>', views.register_login_view, name='register_login'),
    path("password_change/", views.password_change_view, name="password_change"),
    path('change_user_info/', views.change_user_info, name='change-user-info'),
    path("logout/", views.logout_view, name='logout_view'),
    
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reseting-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



    # path("test_login/", views.test_login, name='test_login'),
]
