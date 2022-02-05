from django.urls import path
from .views import RefrigeratorList, Ingredients

urlpatterns = [
    path('list/', RefrigeratorList.as_view(), name = 'ref_door'),
    path('ingre/<int:pk>/', Ingredients.as_view(), name='ingre'),
]