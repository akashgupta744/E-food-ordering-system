from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def booking(request):
    return render(request,'booking.html')

def feature(request):
    return render(request,'feature.html')

def menu(request):
    return render(request,'menu.html')

def single(request):
    return render(request,'single.html')

def team(request):
    return render(request,'team.html')