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

    return render(request,"recipe.html")
