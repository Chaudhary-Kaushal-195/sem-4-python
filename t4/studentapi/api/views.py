from django.shortcuts import render
from rest_framework import viewsets
from api.models import Course,Student
from api.serializers import CourseSerializer,StudentSerializer
# Create your views here.

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class=CourseSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer