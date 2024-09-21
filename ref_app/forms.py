from multiprocessing.dummy import current_process
from django import forms
from .views import *
from .models import IngredientsModel, CompartmentModel, RefrigeratorModel
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
# from bootstrap_datepicker_plus import DatePickerInput


class RefrigeratorCreateForm(forms.ModelForm):
    class Meta:
        model = RefrigeratorModel
        fields = ("name",)

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


class RefrigeratorUpdateForm(forms.ModelForm):
    class Meta:
        model = RefrigeratorModel
        fields = ("name",)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        refrigerator = super().save()
        current_user = self.user
        refrigerator.user.add(current_user)
        if commit:
            refrigerator.save()
        return refrigerator


class CompartmentCrateForm(forms.ModelForm):
    class Meta:
        model = CompartmentModel
        fields = ("name",)

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
        fields = (
            "name",
            "numbers",
            "unit",
            "expiration_date",
        )
        # 入力formに表示させないfields('user', 'compartment')は記載しない
        widgets = {
            "expiration_date": forms.SelectDateWidget(),
        }

    numbers = forms.IntegerField(
        required=True,
        max_value=1000,
        min_value=0,
        label="数量",
    )

    # form オブジェクトを初期化(作成)するときに実行される。
    # 初期化は view 側の get_form_kwargsで与えられた値をもとになされる
    def __init__(self, user, compartment_pk, *args, **kwargs):
        self.user = user
        self.compartment = CompartmentModel.objects.get(pk=compartment_pk)
        super().__init__(*args, **kwargs)

    # form の値の validate 完了後にオブジェクトをセーブするときに実行される
    def save(self, commit=True):
        # まず、saveするオブジェクトを作成する commit=FalseとすることでDBへの保存はまだしない
        ingredients = super().save(commit=False)  # saveするobjectの作成

        # __init__ で設定された user と compartment をsaveするオブジェクトに追加
        ingredients.user = self.user
        ingredients.compartment = self.compartment

        if commit:
            # DBに保存する
            ingredients.save()
        return ingredients

    def clean(self):
        current_user = self.user
        input_name = self.cleaned_data["name"]
        exist_ingre = IngredientsModel.objects.filter(user_id=current_user.id)
        for ck_name in exist_ingre:
            if ck_name.name == input_name:
                raise forms.ValidationError("同じ名前の材料を作成することはできません")
                return self.cleaned_data


class IngredientsUpdateForm(forms.ModelForm):
    class Meta:
        model = IngredientsModel
        fields = (
            "name",
            "numbers",
            "unit",
            "expiration_date",
        )
        widgets = {
            "expiration_date": forms.SelectDateWidget(),
        }

    numbers = forms.IntegerField(
        required=True,
        max_value=1000,
        min_value=0,
        label="数量",
    )

    def __init__(self, user, compartment_pk, *args, **kwargs):
        self.user = user
        self.compartment = CompartmentModel.objects.get(pk=compartment_pk)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        ingredients = super().save(commit=False)
        ingredients.user = self.user
        ingredients.compartment = self.compartment

        if commit:
            ingredients.save()
        return ingredients


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class PasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        self.user.check_password = old_password
        super().clean_old_password(self)
