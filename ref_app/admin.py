from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(RefrigeratorModel)
admin.site.register(CompartmentModel)
admin.site.register(IngredientsModel)
admin.site.register(InfomationModel)
admin.site.register(TodaysRecipeModel)
admin.site.register(IngredientsHistoryModel)
