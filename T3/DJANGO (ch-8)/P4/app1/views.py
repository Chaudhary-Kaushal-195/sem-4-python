from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    search_term = request.GET.get('search','')
    if search_term:
        students = Student.objects.filter(name__icontains=search_term)
    else:
        students = Student.objects.all()
    return render(request, 'home.html', {'students': students})
def details(request, student_id):
    st = Student.objects.get(pk=student_id)
    return render(request, 'details.html', {'student': st})