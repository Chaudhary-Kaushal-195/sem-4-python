from django.shortcuts import render,get_object_or_404,redirect
from student.models import Student
# Create your views here.
def home(request):
    data=Student.objects.all()
    return render(request,"home.html",{'data':data})

def info(request,id):
    marks=get_object_or_404(Student,id=id)
    return render(request,'info.html',{"m":marks})

def add(request):
    if request.method=="POST":
        name=request.POST["name"]
        score=request.POST["score"]
        sub=request.POST["sub"]
        Student.objects.create(name=name,score=score,sub=sub)
        
        return redirect('home')
    return render(request,'add.html')

def edit(request,id):
    stu=get_object_or_404(Student,id=id)
    if request.method=="POST":
        stu.name=request.POST["name"]
        stu.score=request.POST["score"]
        stu.sub=request.POST["sub"]
        stu.save()        
        return redirect('home')
    return render(request,'edit.html',{"stu":stu})

def dele(request,id):
    st=get_object_or_404(Student,id=id)
    st.delete()
    return redirect('home')