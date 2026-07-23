from django.urls import path
from cricapp.views import home, details, addnew ,edit,dele
urlpatterns = [
    path('', home , name='home'),
    path('details/<int:player_id>/', details , name='details'),
    path('addnew/', addnew , name='addnew'),
    path('edit/<int:player_id>/', edit , name='edit'),
    path('dele/<int:player_id>/', dele , name='dele'),

]
