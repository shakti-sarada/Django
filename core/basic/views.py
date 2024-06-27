from django.shortcuts import render,redirect
from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client


def send_email(request):
    send_email_to_client()
    return redirect('/')

def hello(request):

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