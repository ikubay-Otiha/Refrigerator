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
        refrigerator = super().save(commit=False)
        refrigerator.save()
        current_user = self.user
        user = User.objects.filter(id=current_user.id)
        ins = RefrigeratorModel.objects.create(
            user = user
        )
        ins.user.set(user)

        if commit:
            refrigerator.save()
            super()._save_m2m()
        return refrigerator

class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('name', 'numbers', 'unit', 'expiration_date',)
        # 入力formに表示させないfields('user', 'compartment')は記載しない
        widgets = {
            'expiration_date' : forms.SelectDateWidget(),
        }
    def __init__(self, user, compartment_pk, *args, **kwargs):
        self.user = user
        self.compartment = CompartmentModel.objects.get(pk=compartment_pk)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        ingredients = super().save(commit=False) #saveするobjectの作成
        ingredients.user = self.user
        ingredients.compartment = self.compartment

        if commit:
            ingredients.save()
        return ingredients

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