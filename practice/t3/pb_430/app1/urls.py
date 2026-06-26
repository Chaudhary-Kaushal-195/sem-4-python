from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('pb-430/', views.pb_430, name='pb-430'),
    path('about/', views.about, name='about')
]
