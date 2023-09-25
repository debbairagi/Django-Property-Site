from django.urls import path
from crudapp import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('msgs/',views.view_contact_message, name='view_contact_message'),
    path('msgs/<int:pk>/',views.view_single_message, name='msgs'),
    path('agents/', views.view_agent, name='view_agent'),
    path('agents/<int:pk>/', views.view_agent_single, name='agent'),
]