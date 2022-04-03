from django import forms
from .models import IngredientsModel
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('__all__')
        widgets = {
            'expiration_date' : forms.SelectDateWidget(),
        }

class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('expiration_date',)
        widgets = {
            'expiration_date' : forms.SelectDateWidget(),
        }
        