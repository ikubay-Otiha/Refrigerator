from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeList.as_view(), name = 'home'),

    path('ref/', RefrigeratorList.as_view(), name = 'ref'),
    path('create_ref/', RefrigeratorCreate.as_view(), name = 'create_ref'),
    path('delete_ref/<int:pk>/', RefrigeratorDelete.as_view(), name= 'delete_ref'),
    path('update_ref/<int:pk>/', RefrigeratorUpdate.as_view(), name= 'update_ref'),

    path('cpmt_list/<int:pk>/', CompartmentList.as_view(), name = 'cpmt'),
    path('create_cpmt/', CompartmentCreate.as_view(), name = 'create_cpmt'),
    path('update_cpmt/<int:pk>/', CompartmentUpdate.as_view(), name = 'update_cpmt'),
    path('delete_cpmt/<int:pk>/', CompartmentDelete.as_view(), name = 'delete_cpmt'),

    path('ingre/<int:pk>/', Ingredients.as_view(), name='ingre'),
    path('create_ingre/', IngredientsCreate.as_view(), name= 'create_ingre'),
    path('update_ingre/<int:pk>/', IngredientsUpdate.as_view(), name= 'update_ingre'),
    path('delete_ingre/<int:pk>/', IngredientsDelete.as_view(), name= 'delete_ingre'),

    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),

    path('signup/', signupview, name='signup'),

]