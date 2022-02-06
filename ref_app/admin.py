from django.contrib import admin
from .models import RefrigeratorModel, CompartmentModel, IngredientsModel

# Register your models here.

admin.site.register(RefrigeratorModel)
admin.site.register(CompartmentModel)
admin.site.register(IngredientsModel)