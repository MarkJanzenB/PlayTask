from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Assuming views.py is in the same directory

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),  # URL for registration
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
