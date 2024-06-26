from django.utils.text import slugify
import uuid

"""

A function to generate slugfor the recipe model to return string

"""
def generate_slug(title:str)->str:
    from .models import recipe
    title = slugify(title)
    
    while(recipe.objects.filter(slug = title).exists()):
        title = f'{slugify(title)}-{str(uuid.uuid4())[:4]}'
    return title