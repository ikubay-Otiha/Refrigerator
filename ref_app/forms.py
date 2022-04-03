from django import forms
from .models import IngredientsModel
from django.contrib.admin.widgets import AdminDateWidget

class IngredientsCreateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('expiration_date',)
        widgets = {
            'expiration_date' : AdminDateWidget(),
        }

class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = ('expiration_date',)
        widgets = {
            'expiration_date' : AdminDateWidget(),
        }
        