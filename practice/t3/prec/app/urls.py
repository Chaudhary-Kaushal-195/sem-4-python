from django.contrib import admin
from django.urls import path
from app.views import p1 
from app.views import p2

urlpatterns = [
   path('p1/', p1, name='p1'),
   path('p2/', p2, name='p2')
]