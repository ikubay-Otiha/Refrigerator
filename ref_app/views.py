from datetime import datetime
from pipes import Template
from re import template
from sre_constants import SUCCESS
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models, IntegrityError
from .models import RefrigeratorModel, CompartmentModel, IngredientsModel, SalesInfoModel, TodaysRecipeModel #←tentatively#
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
            return RefrigeratorModel.objects.filter(user=current_user.id)
    # Added on2/13

class RefrigeratorCreate(CreateView):
    template_name = 'create_refrigerator.html'
    model = RefrigeratorModel
    fields = ('name','user')
    success_url = reverse_lazy('ref')   
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        context['hoge'] = "fuga"
        print(context['form'].fields['user'])
        print(context['form'].fields['name'])
        print(context['form'].fields['name'])
        context['form'].fields['user'].queryset = User.objects.filter(id=current_user.id)
        return context
    # UrlsのCompartmentCreate.as_view()のメソッドが実行されると、
    # get_context_data(self, **kwargs):も続いて実行される

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
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # context['now'] = datetime.datetime.now()
        # return context
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return CompartmentModel.objects.all()
        else:
            return CompartmentModel.objects.filter(user_id=current_user.id)
    # Added on2/16
    
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
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return IngredientsModel.objects.all()
        else:
            return IngredientsModel.objects.filter(id=current_user.id)
    # Added on2/14
    alarm = []
    expiration = IngredientsModel.expiration_date
    today = datetime.datetime.today()
    # difference = expiration - today
    # if difference < 0:
        # alarm['expiration_alarm'] = (f"{IngredientsModel.objects.name}は賞味期限切れです。")
        # print(alarm)

class IngredientsCreate(CreateView):
    template_name =''
    model = IngredientsModel
    fields =('name', 'compartment', 'numbers', 'unit', 'expiration_date')
    # success_url = reverse_lazy('ingre')

class IngredientsUpdate(UpdateView):
    template_name = ''
    model = IngredientsModel
    # success_url = reverse_lazy('ingre')

class IngredientsDelete(DeleteView):
    template_name = ''
    model = IngredientsModel
    # success_url = reverse_lazy('ingre')

def loginview(request):
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        user = authenticate(request, username=username_data, password=password_data)
        if user is not None:
            login(request, user)
            return redirect('ref')
        else:
            return redirect('login')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('login')

def signupview(request):
    print(request.POST.get('username_data'))
    print(request.POST.get('password_data'))
    if request.method == 'POST':
        username_data = request.POST['username_data']
        password_data = request.POST['password_data']
        # user = User.objects.create_user(username_data, '', password_data)
        try:
            User.objects.create_user(username_data, '', password_data)
        except IntegrityError:
            return render(request, 'signup.html', {'error':'This user was already registered.'})
    else:
        print(User.objects.all())
        return render(request, 'signup.html', {})
    return redirect('login')
    # return render(request, 'login.html', {"you":request.POST.get('username_data')})