from django.shortcuts import render

from django.http import HttpResponse

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