from django.urls import path
from .views import Createcompartment, RefrigeratorList, CompartmentList, Ingredients

urlpatterns = [
    path('', RefrigeratorList.as_view(), name = 'ref'),
    path('cpmt_list/', CompartmentList.as_view(), name = 'cpmt'),
    path('ingre/<int:pk>/', Ingredients.as_view(), name='ingre'),
    path('create_cpmt/', Createcompartment.as_view(), name = 'create_cpmt'),
]