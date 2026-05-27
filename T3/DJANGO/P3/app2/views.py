from django.shortcuts import render

# Create your views here.
def content(request):
    return render(request, 'app2/content.html')

def hello(request):
    return render(request, 'app2/hello.html')

# def home1(request):
#     return render(request, 'app2/home.html')
def home(request):
    return render(request, 'app2/home.html')