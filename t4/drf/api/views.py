from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from api.models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import StudentSerializer
# Create your views here.
@api_view(['GET','POST'])
def home(request):
    if request.method=="GET":
        student = Student.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    
    elif request.method=="POST":
        student = Student.objects.all()
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)