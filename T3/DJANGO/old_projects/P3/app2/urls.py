from django.urls import path
from app2.views import home, content, hello

app_name = 'app2'

urlpatterns = [
    path('home/', home, name='home'),
    path('content/', content, name='content'),
    path('hello/', hello, name='hello'),
]