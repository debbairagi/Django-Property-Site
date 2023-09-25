from django.urls import path
from userapp import views

urlpatterns = [
    path('login/', views.userapp_login, name='userapp_login'),
    path('register/', views.userapp_register, name='userapp_register'),
    path('logout/', views.userapp_logout, name='userapp_logout'),
    path('agent-create/', views.userapp_agent_form, name='userapp_agent_form'),
]