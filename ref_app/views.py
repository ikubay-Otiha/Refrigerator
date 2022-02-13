# from asyncio.windows_events import NULL
from datetime import datetime
from pipes import Template
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models
from .models import RefrigeratorModel, CompartmentModel, IngredientsModel, SalesInfoModel, TodaysRecipeModel #←tentatively#
from django.contrib.auth.models import User
import datetime
# Create your views here.

class RefrigeratorList(ListView):
    template_name = 'refrigerator.html'
    model = RefrigeratorModel
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return RefrigeratorModel.objects.all()
        else:
            return RefrigeratorModel.objects.filter(author=current_user.id)
    # Added on2/13

class RefrigeratorCreate(CreateView):
    template_name = 'create_refrigerator.html'
    model = RefrigeratorModel
    fields = ('name', 'user')
    success_url = reverse_lazy('ref')

class RefrigeratorUpdate(UpdateView):
    template_name = ''
    model = RefrigeratorModel
    fields = ('name', 'user')

class RefrigeratorDelete(DeleteView):
    template_name = ''
    model = RefrigeratorModel
    success_url = reverse_lazy('ref')

class CompartmentList(ListView):
    template_name = 'compartment.html' #←　ref_door.html
    model = CompartmentModel
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        return context
        # viewsで指定した変数をhtmlへ渡すことができる
        # ex)現在時刻など、自分が付加しないデータを渡せる
    # def get_queryset(self):
    #     query_set = self.model.objects.filter(doorname = '肉冷凍室')
    #     return query_set
    #     # あるユーザーの冷蔵庫一覧を取りたい時など。
    #     # あるユーザーの、あるリクエストに対して指定する。等(今回はobject_list)
    #     # ListViewの中の関数をチェックorGoogle.

class CompartmentCreate(CreateView):
    template_name = 'create_compartment.html' #←　create_door.html
    model = CompartmentModel
    fields = ('name', 'refrigerator')
    success_url = reverse_lazy('cpmt')

class CompartmentUpdate(UpdateView):
    template_name = ''
    model = CompartmentModel
    fields = ('name', 'refrigerator')
    success_url = reverse_lazy('cpmt')

class CompartmentDelete(DeleteView):
    template_name = ''
    model = CompartmentModel
    success_url = reverse_lazy('cpmt')

class Ingredients(ListView):
    template_name = 'ingredients.html' 
    model = IngredientsModel
    alarm = []
    expiration = IngredientsModel.expiration_date
    today = datetime.datetime.today()
    # difference = expiration - today
    # if difference < 0:
    #     alarm['expiration_alarm'] = (f"{IngredientsModel.objects.name}は賞味期限切れです。")
    #     print(alarm)

class IngredientsCreate(CreateView):
    template_name =''
    model = IngredientsModel
    fields =('name', 'compartment', 'numbers', 'unit', 'expiration_date')
    # success_url = reverse_lazy('ingre')

class IngredientsUpdate(UpdateView):
    template_name = ''
    model = IngredientsModel
    # success_url = reverse_lazy('ingre')

class IngredientsDetele(DeleteView):
    template_name = ''
    model = IngredientsModel
    # success_url = reverse_lazy('ingre')


