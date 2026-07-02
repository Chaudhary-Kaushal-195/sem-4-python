from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from API.models import Player
from API.serializers import PlayerSerializer
# Create your views here.

@api_view(["GET","POST","PUT","DELETE","PATCH"])
def api_demo(request):
    if request.method=="GET":
        player = Player.objects.all()
        serializer=PlayerSerializer(player,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        player = Player.objects.all()
        serializer=PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(["GET"])
def api_detail(request,id):
    try:
        player=Player.objects.get(id=id)
    
    except:
        return Response({"message":"record not found"},status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
        serializer=PlayerSerializer(player)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=PlayerSerializer(Player,data=serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    elif request.method=="DELETE":
        player.delete()
        return Response({"message":"bye bye"},status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=="PATCH":
        serializer=PlayerSerializer(player,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)