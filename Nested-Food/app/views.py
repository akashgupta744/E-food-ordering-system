from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib import messages
from .models import *
from django.contrib.auth import login,authenticate,logout
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact_us(request):
    d={}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')

        obj = Contact(name=name,email=email,subject=sub,message=msg)
        obj.save()
        d['message']=f'Dear {name} ,Thanks for your time !!'
        
    return render(request,'contact.html',d)

def register(request):
    d={}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('mobile')
        password = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
        if password == password2:
            try:
                usr = User.objects.create_user(username=email,email=email,password=password)
                usr.first_name = name
                usr.save()
                
                profile = Profile(user=usr,contact=number)
                profile.save()
                d['status1'] = f"Dear {name}, Register Successfully !!"
            except :
                d['status2'] = f"Dear {name},This email already exists !!"
        else:
            messages.warning(request,'Passwords do not match!!')
            return redirect('/register')


    return render(request,'register.html',d)

def signin(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('pass1')

        chech_user = authenticate(username=email,password=passw)
        if chech_user:
            login(chech_user)
            context.update({'message':'Login successfull !!','class':'alert-success'})
        else:
            context.update({'message':'Invalid Credentials !!','class':'alert-danger'})

    return render(request,'login.html',context)


def booking(request):
    return render(request,'booking.html')

def feature(request):
    return render(request,'feature.html')

def menu(request):
    if request.method == "POST":
        pass
    else:
        Cat = Category.objects.all()
    return render(request,'menu.html',{'category':Cat})

def single(request):
    return render(request,'single.html')

def team(request):
    return render(request,'team.html')

def dish(request,id):
    c=Category.objects.get(pk=id)
    d=Dish.objects.filter(category=c)
    return render(request,'dish.html',{'dish':d})
