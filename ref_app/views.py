from datetime import datetime
from http.client import REQUEST_URI_TOO_LONG
from pipes import Template
from re import template
from sre_constants import SUCCESS
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.db import models, IntegrityError
from .models import RefrigeratorModel, CompartmentModel, IngredientsModel, SalesInfoModel, TodaysRecipeModel #←tentatively#
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
# Create your views here.
# MyModel._meta.get_fields()
class HomeList(ListView):
    template_name = 'base.html'
    queryset = User.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.user
        
        return context
class RefrigeratorList(ListView):
    template_name = 'refrigerator.html'
    model = RefrigeratorModel
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return RefrigeratorModel.objects.all().order_by('date').reverse
        else:
            return RefrigeratorModel.objects.filter(user=current_user.id).order_by('date').reverse
        return HttpResponseForbidden
    # Added on2/13

class RefrigeratorCreate(CreateView):
    template_name = 'create_refrigerator.html'
    model = RefrigeratorModel
    fields = ('name','user')
    success_url = reverse_lazy('ref')   
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        # ⬆️親クラス（CreateView）のmethodを実行している
        if current_user.is_superuser:
            return context
        else:
            context['form'].fields['user'].queryset = User.objects.filter(id=current_user.id)
            return context
    # UrlsのCompartmentCreate.as_view()のメソッドが実行されると、
    # get_context_data(self, **kwargs):も続いて実行される

class RefrigeratorUpdate(UpdateView):
    template_name = 'update_refrigerator.html'
    model = RefrigeratorModel
    fields = ('name', 'user')
    success_url = reverse_lazy('ref')
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        if current_user.is_superuser:
            return context
        else:    
            context['form'].fields['user'].queryset = User.objects.filter(id=current_user.id)
            return context
class RefrigeratorDelete(DeleteView):
    template_name = 'delete_refrigerator.html'
    model = RefrigeratorModel
    success_url = reverse_lazy('ref')
    # class-based版のredirect()と考える。リダイレクト先のURLを指定

class CompartmentList(ListView):
    template_name = 'compartment.html' #←　ref_door.html
    model = CompartmentModel
    def get_queryset(self):
        current_user = self.request.user
        current_user.id = self.request.user.id
        queryset6 = User.objects.filter(id=current_user.id)
        ref_owner = queryset6[0].id   
        if current_user.is_superuser:
            return CompartmentModel.objects.all().order_by('date').reverse()
        elif self.request.user.id == ref_owner:
            return CompartmentModel.objects.filter(refrigerator_id=self.kwargs['pk']).order_by('date').reverse()
        # CompartmentModel.objects.filter(refrigerator_id=current_user.id, ).order_by('date').reverse()
  
    def get_cotext_data(self, **kwargs):
        current_user = self.request.user
        current_user.id = self.request.user.id
        queryset = User.objects.filter(id=current_user.id)
        ref_owner = queryset[0].id
        context = super().get_context_data(**kwargs)
        cpmt_list = CompartmentModel.objects.filter(id=self.kwargs['pk'])
        context['form'] = cpmt_list
        context["ref_pk"] = ref_owner
        return context

    # アクセスしてきたユーザがその冷蔵庫の所有者か調べる(そうだったら処理継続、違ったら弾く)
    # 仕込んだpkをもとに表示するCompartmentを絞る
    # Added on2/23 CompartmentModel.refrigetaor_idが冷蔵庫所有者をしめす。

    # get_context_data : viewsで指定した変数をhtmlへ渡すことができる
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
    def get_queryset(self):
        # ref_pk = RefrigeratorModel.objects.filter(id=self.kwargs["pk"])
        return RefrigeratorModel.objects.all()
    def get_success_url(self):
        return reverse('cpmt', self.object.refrigerator.id)
            
class CompartmentUpdate(UpdateView):
    template_name = 'update_compartment.html'
    model = CompartmentModel
    fields = ('name', 'refrigerator')
    def get_success_url(self):
        return reverse('cpmt', kwargs={'pk':self.object.refrigerator_id})

class CompartmentDelete(DeleteView):
    template_name = 'delete_compartment.html'
    model = CompartmentModel
    def get_success_url(self):
        return reverse('cpmt', kwargs={'pk':self.object.refrigerator_id})

class Ingredients(ListView):
    template_name = 'ingredients.html' 
    model = IngredientsModel
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return IngredientsModel.objects.all().order_by('date').reverse()
        else:
            return IngredientsModel.objects.filter(id=current_user.id)
    # Added on2/14
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        over_expiration_items = list()
        # context['object_list'] はget_querysetの結果得られた IngredientsModelのlist
        for ingredient in context['object_list']:
            expiration = ingredient.expiration_date
            today = datetime.date.today()
            difference = expiration - today
            over_expiration = difference < datetime.timedelta(0)
            if over_expiration:
                over_expiration_items.append(ingredient)
                ingredient.is_over_expiration = True
        context['over_expiration_items'] = over_expiration_items
        return context

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
            return redirect('home')
            # redirectでどのURLを開くか指定（ここではref）
            # 1st-argument:移動先URLを指定
            # 2nd-argument:urlsに渡す変数を定義
        else:
            return redirect('login')
    return render(request, 'login.html')
    # renderで結果をWebPageに表示
    # ex) return render(request, template, context)
    # 1st-argument:requestオブジェクトを受け取る
    # 2nd-argument:表示するテンプレートを指定
    # 3rd-argument:テンプレートに渡す変数を指定

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