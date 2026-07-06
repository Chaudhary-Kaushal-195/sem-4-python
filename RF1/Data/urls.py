
from django.urls import path
from Data.views import home,add,edit,dele

urlpatterns = [
    
    path("home/",home,name='home'),
    path("add/",add,name="add"),
    path("edit/<str:name>",edit,name="edit"),
    path("dele/<str:name>",dele,name="dele")
    
]