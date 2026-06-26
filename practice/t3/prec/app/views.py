from django.shortcuts import render

# Create your views here.
def p1(request):
    return render(request, 'p1.html')

def p2(request):
    return render(request, 'p2.html')