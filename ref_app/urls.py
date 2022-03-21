from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeList.as_view(), name = 'home'),

    path('ref/', RefrigeratorList.as_view(), name = 'ref'),
    path('detail_ref/<int:pk>/', RefrigeratorDetail.as_view(), name = 'detail_ref'),
    path('create_ref/', RefrigeratorCreate.as_view(), name = 'create_ref'),
    path('delete_ref/<int:pk>/', RefrigeratorDelete.as_view(), name= 'delete_ref'),
    path('update_ref/<int:pk>/', RefrigeratorUpdate.as_view(), name= 'update_ref'),

    # path('cpmt_list/<int:pk>/', CompartmentList.as_view(), name = 'cpmt'),
    path('cpmt_detail/<int:pk>/', CompartmentDetail.as_view(), name = 'cpmt_detail'),
    path('create_cpmt/<int:ref_pk>', CompartmentCreate.as_view(), name = 'create_cpmt'),
    path('update_cpmt/<int:pk>/', CompartmentUpdate.as_view(), name = 'update_cpmt'),
    path('delete_cpmt/<int:pk>/', CompartmentDelete.as_view(), name = 'delete_cpmt'),

    path('ingre/<int:pk>/', Ingredients.as_view(), name='ingre'),
    # path('ingre/<int:pk>/', IngredientsDetail.as_view(), name='ingre'),
    path('create_ingre/', IngredientsCreate.as_view(), name= 'create_ingre'),
    path('update_ingre/<int:pk>/', IngredientsUpdate.as_view(), name= 'update_ingre'),
    path('delete_ingre/<int:pk>/', IngredientsDelete.as_view(), name= 'delete_ingre'),
    path('create_ingre_history/', IngredientsHistoryCreate.as_view(), name= 'create_history_ing'),

    path('info/', InfomationList.as_view(), name= 'info'),
    path('create_info/', InfomationCreate.as_view(), name= 'create_info'),
    path('update_info/<int:pk>/', InfomationUpdate.as_view(), name= 'update_info'),
    path('delete_info/<int:pk>/', InfomationDelete.as_view(), name= 'delete_info'),

    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),

    path('signup/', signupview, name='signup'),

    path('html_test', Test.as_view(), name='test')
]