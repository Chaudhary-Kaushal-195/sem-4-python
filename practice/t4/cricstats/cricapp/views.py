from django.shortcuts import render , redirect ,get_list_or_404
from cricapp.models import Data
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    search=request.GET.get('name')
    if search:
        data=Data.objects.filter(name__icontains=search)
    else:
        data=Data.objects.all()
    return render(request,'home.html',{'data':data})

def addnew(request):
    if request.method == "POST":
        name = request.POST["name"]
        country = request.POST["country"]
        bas = request.POST["bas"]
        bos = request.POST["bos"]
        age = request.POST["age"]
        rs = request.POST["rs"]
        wt = request.POST["wt"]

        Data.objects.create(
            name=name,
            country=country,
            bas=bas,
            bos=bos,
            age=age,
            rs=rs,
            wt=wt
        )
        return redirect('home')

    return render(request,'addnew.html')

def details(request, player_id):
    player = Data.objects.get(id=player_id)
    return render(request,'details.html', {'player': player})

def edit(request, player_id):
    player = Data.objects.get(id=player_id)
    if request.method == "POST":
        player.name = request.POST["name"]
        player.country = request.POST["country"]
        player.bas = request.POST["bas"]
        player.bos = request.POST["bos"]
        player.age = request.POST["age"]
        player.rs = request.POST["rs"]
        player.wt = request.POST["wt"]
        player.save()
        return redirect('home')
    return render(request, 'edit.html', {'player': player})

def dele(request, player_id):
    player = Data.objects.get(id=player_id)
    player.delete()
    return redirect('home')