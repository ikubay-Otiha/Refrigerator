from django.urls import path
from .views import *

urlpatterns = [
    path('', RefrigeratorList.as_view(), name = 'ref'),
    path('create_ref/', RefrigeratorCreate.as_view(), name = 'create_ref'),
    path('delete_ref/', RefrigeratorDelete.as_view(), name= 'delete_ref'),
    path('update_ref/', RefrigeratorUpdate.as_view(), name= 'update_ref'),

    path('cpmt_list/', CompartmentList.as_view(), name = 'cpmt'),
    path('create_cpmt/', CompartmentCreate.as_view(), name = 'create_cpmt'),
    path('update_cpmt/', CompartmentUpdate.as_view(), name = 'update_cpmt'),
    path('delete_cpmt/', CompartmentDelete.as_view(), name = 'delete_cpmt'),
    
    path('ingre/<int:pk>', Ingredients.as_view(), name='ingre'),
    path('create_ingre/', IngredientsCreate.as_view(), name= 'create_ingre'),



]