from django.shortcuts import render,redirect
from django.http import HttpResponse
from vege.seed import *
from .utils import send_emai_with_attachment
from .models import Car


def send_email(request):
    subject = "Test Email"
    message = "Django server email test."
    recipient_list = ["shaktisahoo65@gmail.com"]
    file_path = r"C:\Users\dell\Downloads\sushi.jpg"
    send_emai_with_attachment(subject,message,recipient_list,file_path)
    return redirect('/')

def hello(request):

    Car.objects.create(name = f"Supra-{random.randint(0,100)}")

    peoples=[
        {'name':'Shakti','age':22},
        {'name':'Siddarth','age':22},
        {'name':'Ayushman','age':17},
        {'name':'Ronit','age':15},
        {'name':'Alok','age':19},
        {'name':'Rohit','age':20},
    ]



    return render(request,"index.html",context={'peoples':peoples,'page':'Home'})


def contact(request):
    context={'page':'Contact'}
    
    return render(request,"contact.html",context)

def about(request):
    context={'page':'About'}
    
    return render(request,"about.html",context)