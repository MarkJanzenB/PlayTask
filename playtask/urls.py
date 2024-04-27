from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('project/read/', views.project_list_view, name='project_list'),
    path('project/read/<int:pk>/', views.project_detail_view, name='project_detail'),
    path('project/create/', views.project_create_view, name='project_create'),
    path('project/<int:pk>/update/', views.project_edit_view, name='project_edit'),  # Added for editing
    path('project/<int:pk>/delete/confirm/', views.project_confirm_delete_view, name='project_confirm_delete'),
    path('project/<int:pk>/delete/', views.project_delete_view, name='project_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
