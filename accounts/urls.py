from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile2/', views.profile_view, name='profile2'),
    
]
