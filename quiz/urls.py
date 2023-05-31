from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('tests/', views.test_list, name='test_list'),
    path('<int:pk>/', views.test_detail, name='test_detail'),
    path('<int:pk>/result/', views.test_result, name='test_result'),
    path('statistics/', views.statistics, name='statistics'),
]
