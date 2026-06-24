from django.urls import path
from .views import home,info,add,edit,dele

urlpatterns = [
    path("",home,name="home"),
    path("info/<int:id>",info,name='info'),
    path("add/",add,name='add'),
    path("edit/<int:id>",edit,name='edit'),
    path("dele/<int:id>",dele,name="dele")
]