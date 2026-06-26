from django.shortcuts import render

# Create your views here.


def pb_430(request):
    return render(request, 'pb-430.html')

def about(request):
    return render(request, 'about.html')