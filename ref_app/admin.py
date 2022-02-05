from django.contrib import admin
from .models import RefrigeratorModel,IngredientsModel

# Register your models here.

admin.site.register(RefrigeratorModel)
admin.site.register(IngredientsModel)