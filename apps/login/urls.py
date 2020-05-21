from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.signup, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]