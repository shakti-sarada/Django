from django.shortcuts import render,redirect
from .models import *

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
    context = {'recipes' : queryset}


    return render(request,"recipe.html",context)


def delete_recipe(request,id):
    queryset = recipe.objects.get(id=id) #Getting Dynamically Id
    queryset.delete()
    return redirect('/recipe/')