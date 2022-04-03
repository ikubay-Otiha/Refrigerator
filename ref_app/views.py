from datetime import datetime
from multiprocessing import cpu_count
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy, reverse
from django.db import models, IntegrityError
from .models import IngredientsHistoryModel, RefrigeratorModel, CompartmentModel, IngredientsModel, InfomationModel, SalesInfoModel, TodaysRecipeModel #←tentatively#
from .forms import IngredientsCreateForm, IngredientsUpdateForm
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
        context['filter'] = User.objects.all()
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
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        if current_user.is_superuser:
            context['name'] = self.request.user
            context['filter_date'] = RefrigeratorModel.objects.all().order_by('date')
            context['filter_name'] = RefrigeratorModel.objects.all().order_by('name').reverse
            return context
        else:
            context['name'] = self.request.user
            context['filter_date'] = RefrigeratorModel.objects.filter(user=current_user.id).order_by('date')
            context['filter_name'] = RefrigeratorModel.objects.filter(user=current_user.id).order_by('name').reverse
            return context

class RefrigeratorDetail(DetailView):
    template_name = 'refrigerator_detail.html'
    model = RefrigeratorModel

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['name'] = self.request.user
        # ctx['cpmt_numbers'] = 
        ctx['child_cpmt'] = CompartmentModel.objects.filter(refrigerator=self.get_object())
        ing_quantity = list()
        for i in ctx['child_cpmt']:
            counts = i.id
            ingre_quantity = IngredientsModel.objects.filter(compartment=counts).count()
            ing_quantity.append(ingre_quantity)
            continue
        ctx['ing_quantity'] = ing_quantity
        return ctx

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
        return HttpResponseForbidden
        
class RefrigeratorDelete(DeleteView):
    template_name = 'delete_refrigerator.html'
    model = RefrigeratorModel
    success_url = reverse_lazy('ref')
    # success_url = reverse_lazy('ref', kwargs={'filter': 'filter'})
    # class-based版のredirect()と考える。リダイレクト先のURLを指定

class CompartmentDetail(DetailView):
    template_name = 'compartment_detail.html'
    model = CompartmentModel
    def get_context_data(self, **kwargs):
        get_cpmt = self.get_object()
        ctx = super().get_context_data(**kwargs)
        ctx['name'] = self.request.user
        ctx['child_ingredients'] = IngredientsModel.objects.filter(compartment=self.get_object())
        ctx['update_ingre'] = IngredientsHistoryModel.objects.filter(ingre_cpmt=self.get_object())
        ctx['get_cpmt'] = get_cpmt
        ctx['test'] = CompartmentModel.objects.filter(id=self.object.id)
        return ctx

class CompartmentCreate(CreateView):
    template_name = 'create_compartment.html' #←　create_door.html
    model = CompartmentModel
    fields = ('name', 'refrigerator')
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        context['ref_pk'] = self.kwargs['ref_pk']
        if current_user.is_superuser:
            return context
        else:    
            set_ref_owner = User.objects.filter(id=current_user.id)
            context['form'].fields['refrigerator'].queryset = RefrigeratorModel.objects.filter(user=current_user)
            return context
    def get_success_url(self):
        return reverse('detail_ref', kwargs={'pk':self.object.refrigerator_id})

class CompartmentUpdate(UpdateView):
    template_name = 'update_compartment.html'
    model = CompartmentModel
    fields = ('name', 'refrigerator')
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        if current_user.is_superuser:
            return context
        else:    
            context['form'].fields['refrigerator'].queryset = RefrigeratorModel.objects.filter(user=current_user.id)
            return context
    def get_success_url(self):
        return reverse('detail_ref', kwargs={'pk':self.object.refrigerator_id})

class CompartmentDelete(DeleteView):
    template_name = 'delete_compartment.html'
    model = CompartmentModel
    def get_success_url(self):
        return reverse('detail_ref', kwargs={'pk':self.object.refrigerator.id})

class IngredientsDetail(DetailView):
    template_name = 'ingredients.html'
    model = IngredientsModel
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['child_ingredients'] = IngredientsModel.objects.filter(compartment=self.get_object())
        return ctx

class IngredientsCreate(CreateView):
    template_name ='create_ingredients.html'
    model = IngredientsModel
    fields =('name', 'user', 'compartment', 'numbers', 'unit', 'expiration_date')
    def get_queryset(self):
        current_user = self.request.user
        current_user.id = self.request.user.id
        queryset = User.objects.filter(id=current_user.id)
        cpmt_owner = queryset[0].id 
        if current_user.is_superuser:
            return IngredientsModel.objects.all()
        elif self.request.user.id == cpmt_owner:
            return IngredientsModel.objects.filter(refrigerator_id=self.kwargs['pk'])
        return HttpResponseForbidden
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super().get_context_data(**kwargs)
        context['cpmt_pk'] = self.kwargs['cpmt_pk']
        context['add_date_form'] = IngredientsCreateForm()
        if current_user.is_superuser:
            return context
        else:    
            cpmt_pk = context['cpmt_pk']
            context['form'].fields['user'].queryset = User.objects.filter(id=self.request.user.id)
            return context
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        ing_ins = form.instance
        cpmt_id = form.cleaned_data['compartment'].id
        IngredientsHistoryModel.objects.create(
            ingre_name = ing_ins,
            ingre_cpmt = CompartmentModel.objects.get(id=cpmt_id),
            created_at = datetime.datetime.now(),
            ingre_numbers = form.cleaned_data['numbers'],
            ingre_unit = form.cleaned_data['unit'],
            expiration_date = form.cleaned_data['expiration_date'],
        )
        return super().form_valid(form)
        # 自分で指定したModelに右辺を保存。
        # deleteに見せかけたupdateviewを作成。
    def get_success_url(self):
        return reverse_lazy('cpmt_detail', kwargs={'pk' : self.kwargs["cpmt_pk"]})

class IngredientsUpdate(UpdateView):
    template_name = 'update_ingredients.html'
    model = IngredientsModel  
    fields =('name', 'user', 'compartment', 'numbers', 'unit', 'expiration_date')
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        cpmt = self.object.compartment
        context =  super().get_context_data(**kwargs)
        context['cpmt_pk'] = cpmt.pk
        context['add_date_form'] = IngredientsUpdateForm()
        if current_user.is_superuser:
            return context
        else: 
            context['form'].fields['user'].queryset = User.objects.filter(id=self.request.user.id)
            return context
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        ing_ins = form.instance
        cpmt_id = form.cleaned_data['compartment'].id
        IngredientsHistoryModel.objects.create(
            ingre_name = ing_ins,
            ingre_cpmt = CompartmentModel.objects.get(id=cpmt_id),
            updated_at = datetime.datetime.now(),
            ingre_numbers = form.cleaned_data['numbers'],
            ingre_unit = form.cleaned_data['unit'],
            expiration_date = form.cleaned_data['expiration_date'],
        )
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('cpmt_detail', kwargs={'pk' : self.object.compartment.pk})

class IngredientsDelete(DeleteView):
    template_name = 'delete_ingredients.html'
    model = IngredientsModel
    def get_context_data(self, **kwargs):
        cpmt = self.object.compartment
        context =  super().get_context_data(**kwargs)
        context['cpmt_pk'] = cpmt.pk
        return context
    def get_success_url(self):
        cpmt = self.object.compartment
        return reverse_lazy('cpmt_detail', kwargs={'pk' : cpmt.pk})

# Below here, these are InformataionViews.
class InfomationList(ListView):
    template_name = 'info_list.html'
    model = InfomationModel
    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return InfomationModel.objects.all().order_by('date').reverse
        else:
            return InfomationModel.objects.filter(id=current_user.id).order_by('date').reverse
        return HttpResponseForbidden

class InfomationCreate(CreateView):
    template_name = 'create_info.html'
    model = InfomationModel
    fields = ('title', 'text', 'refrigerator')
    success_url = reverse_lazy('info')   

class InfomationUpdate(UpdateView):
    template_name = 'update_info.html'
    model = InfomationModel
    fields = ('title', 'text', 'refrigerator')
    success_url = reverse_lazy('info')

class InfomationDelete(DeleteView):
    template_name = 'delete_info.html'
    model = InfomationModel
    success_url = reverse_lazy('info')

# login,logout,signupview
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

class Test(ListView):
    template_name = "test.html"
    queryset = User.objects.all()

# from path.to.the.model import MyModel # 事前にモデルがimportされていない場合
# MyModel._meta.get_fields()

# ex. User._meta.get_fields()

# Below here, these are not currently used.

# class CompartmentList(ListView):
    # template_name = 'compartment.html' #←　ref_door.html
    # model = CompartmentModel
    # def get_queryset(self):
        # current_user = self.request.user
        # current_user.id = self.request.user.id
        # queryset6 = User.objects.filter(id=current_user.id)
        # ref_owner = queryset6[0].id   
        # if current_user.is_superuser:
            # return CompartmentModel.objects.all().order_by('date').reverse()
        # elif self.request.user.id == ref_owner:
            # return CompartmentModel.objects.filter(refrigerator_id=self.kwargs['pk']).order_by('date').reverse()
        # CompartmentModel.objects.filter(refrigerator_id=current_user.id, ).order_by('date').reverse()
#   
    # def get_cotext_data(self, **kwargs):
        # current_user = self.request.user
        # current_user.id = self.request.user.id
        # queryset = User.objects.filter(id=current_user.id)
        # ref_owner = queryset[0].id
        # context = super().get_context_data(**kwargs)
        # cpmt_list = CompartmentModel.objects.filter(id=self.kwargs['pk'])
        # context['form'] = cpmt_list
        # context["ref_pk"] = ref_owner
        # return context

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
# class Ingredients(ListView):
    # template_name = 'ingredients.html' 
    # model = IngredientsModel
    # def get_queryset(self):
        # current_user = self.request.user
        # if current_user.is_superuser:
            # return IngredientsModel.objects.all().order_by('date').reverse()
        # else:
            # return IngredientsModel.objects.filter(id=current_user.id)
    # Added on2/14
    # def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)
        # over_expiration_items = list()
        # context['object_list'] はget_querysetの結果得られた IngredientsModelのlist
        # for ingredient in context['object_list']:
            # expiration = ingredient.expiration_date
            # today = datetime.date.today()
            # difference = expiration - today
            # over_expiration = difference < datetime.timedelta(0)
            # if over_expiration:
                # over_expiration_items.append(ingredient)
                # ingredient.is_over_expiration = True
        # context['over_expiration_items'] = over_expiration_items
        # context['passed_ing_pk'] = self.kwargs['pk']
        # return context

# class IngredientsHistoryCreate(CreateView):
    # template_name = 'create_ingre_history.html'
    # model = IngredientsHistoryModel
    # fields = ('update_user', 'ingre_name', 'ingre_numbers', 'ingre_unit')
    # success_url = reverse_lazy()
    # 複数行の記載（条件分岐など）によってsuccess_urlが変わるときはget_success_urlを用いる

    # def form_valid(self, form):
        # """If the form is valid, save the associated model."""
        # self.object = form.save()
        # IngredientsHistoryModel.objects.create(
            # update_date = 'update_date',
            # update_user = 'update_user',
            # ingre_name =  'ingre_name',
            # ingre_numbers =  'ingre_numbers',
            # ingre_unit = 'ingre_unit',
        # )
        # 自分で指定したModelに保存。（の中身を）
        # Modelが持っていないカラムは指定できない。
        # update,deleteViewでも同様の記載をする。
        # deleteに見せかけたupdateviewを作成。
        # CompartmentDetailViewで0個のIngredientsを表示させないようにする
        # return super().form_valid(form)
    
    # def form_valid(self, form):
        # pk = self.kwargs.get('pk')
        # ingredients = get_object_or_404(IngredientsModel, pk=pk)
        # update_date = int(self.request.POST.get('update_date'))
        # update_user = self.request.user
        # ingre_name = self.request.POST.get('ingre_name')
        # ingre_numbers = int(self.request.POST.get('ingre_numbers'))
        # ingre_unit = self.request.POST.get('ingre_unit')

        # history = form.save(commit=False)
        # history.ingre = ingredients
        # history.date = update_date
        # history.user = update_user
        # history.ingre_name = ingre_name
        # history.ingre_num = ingre_numbers
        # history.ingre_unit = ingre_unit
        # history.save()
        # return redirect('ingre', pk=pk)
