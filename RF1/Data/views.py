from django.shortcuts import render,get_object_or_404,redirect
from Data.models import Fac
# Create your views here.

def home(request):
    fac=Fac.objects.all()
    return render(request,'home.html',{'fac':fac})

def add(request):
    if request.method=="POST":
        name = request.POST['name']
        subject = request.POST['subject']
        score = request.POST['score']
        grade = request.POST['grade']
        pr_grade = request.POST['pr_grade']
        
        Fac.objects.create(name=name,subject=subject,score=score,grade=grade,pr_grade=pr_grade)
        
        return redirect('home')
    return render(request,'add.html')


def edit(request,name):
    fac=get_object_or_404(Fac,name=name)
    if request.method=="POST":
        fac.name=request.POST["name"]
        fac.subject = request.POST['subject']
        fac.score=request.POST["score"]
        fac.grade = request.POST['grade']
        fac.pr_grade = request.POST['pr_grade']
        fac.save()        
        return redirect('home')
    return render(request,'edit.html',{"fac":fac})


def dele(request,name):
    st=get_object_or_404(Fac,name=name)
    st.delete()
    return redirect('home')