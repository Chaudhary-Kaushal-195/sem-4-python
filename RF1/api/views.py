from django.shortcuts import render
from rest_framework import viewsets
from Data.models import Fac
from api.serializers import FacSerializer

# Create your views here.
class facviewset(viewsets.ModelViewSet):
    queryset=Fac.objects.all
    serializer_class=FacSerializer