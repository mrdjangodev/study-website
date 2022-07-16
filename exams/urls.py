from cgi import test
from django.urls import path
from .views import test_view, save_test_view, score_view


urlpatterns = [
    path('test/<int:pk_id>/', test_view, name='test-view'),
    path('test/<int:pk>/save/', save_test_view, name='save_result'),
    path('score/<int:pk>/', score_view, name='score_page'),
]
