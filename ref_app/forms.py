from django import forms
from .views import *
from .models import IngredientsModel, CompartmentModel, RefrigeratorModel
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RefrigeratorCreateForm(forms.ModelForm):
    class Meta:
        model = RefrigeratorModel
        fields = ('name',)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # many to many はリレーション先を定める前にオブジェクトができている必要あるためcommit=falseしない
        # super().save()の戻り地はrefrigeatorのオブジェクトのため自作する必要なし
        refrigerator = super().save()
        current_user = self.user
        # 単体のオブジェクトの場合はaddを使う
        refrigerator.user.add(current_user)
        if commit:
            refrigerator.save()
        return refrigerator

class CompartmentCrateForm(forms.ModelForm):
    class Meta:
        model = CompartmentModel
        fields = ('name',)

    def __init__(self, refrigerator_pk, *args, **kwargs):
        self.refrigerator = RefrigeratorModel.objects.get(pk=refrigerator_pk)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        compartment = super().save(commit=False)
        compartment.refrigerator = self.refrigerator

        if commit:
            compartment.save()
        return compartment

class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('name', 'numbers', 'unit', 'expiration_date',)
        # 入力formに表示させないfields('user', 'compartment')は記載しない
        widgets = {
            'expiration_date' : forms.SelectDateWidget(),
        }
    # form オブジェクトを初期化(作成)するときに実行される。
    # 初期化は view 側の get_form_kwargsで与えられた値をもとになされる
    def __init__(self, user, compartment_pk, *args, **kwargs):
        self.user = user
        self.compartment = CompartmentModel.objects.get(pk=compartment_pk)
        super().__init__(*args, **kwargs)

    # form の値の validate 完了後にオブジェクトをセーブするときに実行される
    def save(self, commit=True):
        
        # まず、saveするオブジェクトを作成する commit=FalseとすることでDBへの保存はまだしない
        ingredients = super().save(commit=False) #saveするobjectの作成
        
        # __init__ で設定された user と compartment をsaveするオブジェクトに追加
        ingredients.user = self.user
        ingredients.compartment = self.compartment

        if commit:
            # DBに保存する
            ingredients.save()
        return ingredients

class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('expiration_date',)
        widgets = {
            'expiration_date' : forms.SelectDateWidget(),
        }
        
        
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]