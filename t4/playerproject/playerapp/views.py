from django.shortcuts import render,redirect,get_object_or_404
from playerapp.models import Player

# Create your views here.
def home(request):
    search=request.GET.get('name')
    if search:
        play=Player.objects.filter(name__icontains=search)
    else:
        play=Player.objects.all()
    return render(request,'home.html',{'play':play})



def welcome(request):
    return render(request,'welcome.html')



def add(request):
    if request.method=="POST":
        name=request.POST['name']
        innings=request.POST['innings']
        runs=request.POST['runs']
        Player.objects.create(name=name,innings=innings,runs=runs)
        return redirect('home')
    return render(request,'add.html')


def edit(request,id):
    play=get_object_or_404(Player,id=id)
    if request.method=="POST":
        play.name=request.POST['name']
        play.innings=request.POST['innings']
        play.runs=request.POST['runs']
        play.save()
        return redirect('home')
    return render(request,'edit.html',{'play':play})

def dele(request,id):
    play=get_object_or_404(Player,id=id)
    play.delete()
    return redirect('home')