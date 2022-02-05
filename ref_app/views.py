from django.shortcuts import render
from django.views.generic import ListView #←tentatively#
from .models import IngredientsModel, RefrigeratorModel #←tentatively#

# Create your views here.

class RefrigeratorList(ListView):
    template_name = 'ref_door.html' 
    model = RefrigeratorModel

class Ingredients(ListView):
    template_name = 'ingredients.html' 
    model = IngredientsModel