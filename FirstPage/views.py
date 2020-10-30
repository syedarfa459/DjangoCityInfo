from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'firstpage.html')

def home(request):
    return render(request,'home.html')


def services(request):
    return HttpResponse('<h1 style="text-align:center;">Welcome to Our Services')


def contact(request):
    # if form.data['username']


    if request.method=="POST":
        UserName=request.POST.get('username')
        PhoneNumber=request.POST.get('phone')
        City=request.POST.get('city')
        UserAdvice=request.POST.get('useradvice')
        contactinstance=Contact(UserName=UserName,PhoneNumber=PhoneNumber,City=City,Useradvice=UserAdvice)
        contactinstance.save()
        messages.success(request,"Your response has been sent to the server!")
        
    return render(request,'contact.html')

