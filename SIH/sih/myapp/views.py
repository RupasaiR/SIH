from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import register

def register(request):
    if request.method=='POST':
        crop=request.POST.get('crop','')
        rainfall=request.POST.get('rainfall','')
        temp=request.POST.get('temp','')
        ph=request.POST.get('ph','')
        return render(request,'myapp/index.html',{'crop':crop,'rainfall':rainfall,'temp':temp,'ph':ph})
    else:    
        return render(request,'myapp/register.html')
def login(request):
    if request.method=='POST':
        uname=request.POST.get('uname','')
        password=request.POST.get('pass','')
        u=register.create(name=uname,password=password)
        u.save()

        return render(request,'myapp/register.html')
    else:
        return render(request,'myapp/login.html')

