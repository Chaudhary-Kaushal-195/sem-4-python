from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, "home.html") 

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()          # creates the User row, password is hashed
            login(request, user)        # auto-login right after signup (optional)
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        # --- or the manual way, without AuthenticationForm ---
        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # user = authenticate(request, username=username, password=password)
        if form.is_valid():
            user = form.get_user()
            login(request, user)        # starts the session / sets request.user
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)     # clears the session — logs the user out
    return redirect("login")


@login_required(login_url="login")
def dashboard_view(request):
    return render(request, "dashboard.html")

