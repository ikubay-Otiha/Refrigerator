from datetime import datetime
from re import template
from django.shortcuts import render
from django.views.generic import ListView, CreateView #←tentatively#
from django.urls import reverse_lazy
from .models import RefrigeratorModel, CompartmentModel, IngredientsModel #←tentatively#
import datetime
# Create your views here.

# def index(request):
#     door_data = RefrigeratorModel.objects.all()
#     params = {
#         'doorname' : '冷蔵室一覧'
#     }
#     return render(request, '', params)

class RefrigeratorList(ListView):
    # tempalte_name = XXX.html
    model = RefrigeratorModel

class CompartmentList(ListView):
    template_name = 'compartment.html' #←　ref_door.html
    model = CompartmentModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hoge'] = datetime.datetime.now()
        return context
        # viewsで指定した変数をhtmlへ渡すことができる
        # ex)現在時刻など、自分が付加しないデータを渡せる
    # def get_queryset(self):
    #     query_set = self.model.objects.filter(doorname = '肉冷凍室')
    #     return query_set
    #     # あるユーザーの冷蔵庫一覧を取りたい時など。
    #     # あるユーザーの、あるリクエストに対して指定する。等(今回はobject_list)
    #     # ListViewの中の関数をチェックorGoogle.

class Ingredients(ListView):
    template_name = 'ingredients.html' 
    model = IngredientsModel

class Createcompartment(CreateView):
    template_name = 'create_compartment.html' #←　create_door.html
    model = CompartmentModel
    fields = ('name', 'refrigerator')
    success_url = reverse_lazy('ref_door') 