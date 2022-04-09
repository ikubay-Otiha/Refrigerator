from django import forms
from .models import CompartmentModel, IngredientsModel
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        # form に表示させない user と compartment は記載しない
        fields = ('name', 'numbers', 'unit', 'expiration_date')
        widgets = {
            'expiration_date': forms.SelectDateWidget(),
        }

    def __init__(self, user, compartment_pk, *args, **kwargs):
        # form オブジェクトを初期化(作成)するときに実行される。
        # 初期化は view 側の get_form_kwargsで与えられた値をもとになされる
        self.user = user
        self.compartment = CompartmentModel.objects.get(pk=compartment_pk)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        # form の値の validate 完了後にオブジェクトをセーブするときに実行される

        # まず、saveするオブジェクトを作成する commit=FalseとすることでDBへの保存はまだしない
        ingredient = super().save(commit=False)
        # __init__ で設定された user と compartment をsaveするオブジェクトに追加
        ingredient.user = self.user
        ingredient.compartment = self.compartment

        if commit:
            # DBに保存する
            ingredient.save()
        return ingredient

class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('expiration_date',)
        widgets = {
            'expiration_date' : forms.SelectDateWidget(),
        }
        
# class IngredientsCreateSelectForm(forms.ModelForm):
#     class Meta:
#         model = IngredientsModel
#         fields = ('')