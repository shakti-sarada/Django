from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def recipes(request):
    if request.method == "POST":
        data = request.POST

        name = data.get("name")
        description = data.get("description")
        image = request.FILES.get("image")

        recipe.objects.create(
          name=name,
          description=description,
          image=image,  
        )
        
        return redirect('/recipe/')

    queryset = recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    
    
    context = {'recipes' : queryset}
    return render(request,"recipe.html",context)


def delete_recipe(request,id):
    queryset = recipe.objects.get(id=id) #Getting Dynamically Id
    queryset.delete()
    return redirect('/recipe/')

def update_recipe(request,id):
    queryset = recipe.objects.get(id=id) #Getting Dynamically Id

    if request.method=="POST":
        data =request.POST

        name = data.get("name")
        description = data.get("description")
        image = request.FILES.get("image")

        queryset.name = name
        queryset.description = description
        
        if recipe.image:
            queryset.image = image

        queryset.save()
        return redirect('/recipe/')

    context = {'recipe':queryset}
    return render(request,"update_recipes.html",context)



def login_page(request):

    if request.method == "POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')        
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')    

        else:
            login(request,user)
            return redirect('/recipe/')
        
    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')



def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('First Name')
        last_name = request.POST.get('Last Name')
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already exists')
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')

        return redirect('/register/')
    return render(request,'register.html')