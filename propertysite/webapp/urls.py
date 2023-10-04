from django.urls import path
from webapp import views

urlpatterns = [
    path('propertyentry/', views.propertyentryform, name='propertyentryform'),
]

