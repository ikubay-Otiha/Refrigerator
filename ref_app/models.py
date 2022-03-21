from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RefrigeratorModel(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        null=True,
        verbose_name="冷蔵庫名"
    )
    date = models.DateField(auto_now_add=True)
    user = models.ManyToManyField(User, verbose_name="ユーザー")
    # compartment = CompartmentModel.refrigerator_set.all()
    def __str__(self):
        return self.name
    # class Meta:
        # verbose_name_plural =('冷蔵庫')

COMPARTMENT_TYPE = (
    ('Refrigerator','冷蔵室'),('Freezer','冷凍室'),('Vegetable','野菜室'),
    ('Chilled','チルド室'),('Icebox','アイスボックス')
)
class CompartmentModel(models.Model):
    name = models.CharField(
        max_length = 100,
        choices = COMPARTMENT_TYPE,
        verbose_name="冷蔵室名"
    )
    refrigerator = models.ForeignKey(
        RefrigeratorModel, 
        on_delete=models.PROTECT,
        verbose_name="冷蔵庫名")
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.refrigerator.name}/{self.get_name_display()}"

UNIT = (
    ('ko','個'),('fukuro','袋'),('hon','本'),('gram','g'),
    ('kilogram','kg'),('milliliter','ml'),('liter','L')
)
class IngredientsModel(models.Model):
    name = models.CharField(max_length=200,verbose_name="材料名")
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    compartment = models.ManyToManyField(
        CompartmentModel,
        related_name='ing_cpmt',
        verbose_name="対象冷蔵室"
    )
    # 一対多の場合:食材が多になる、キーは多につける。
    numbers = models.IntegerField(verbose_name="数量")
    unit = models.CharField(
        max_length = 50,
        choices = UNIT,
        verbose_name="単位"
    )
    date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(verbose_name="賞味期限")
    def __str__(self):
        return self.name

class IngredientsHistoryModel(models.Model):
    ingre_name = models.OneToOneField(
        IngredientsModel,
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name="食材名",
        related_name='history_ing_name'
    )
    ingre_cpmt = models.ForeignKey(
        IngredientsModel,
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name="冷蔵室名",
        related_name='history_ing_cpmt'
    )
    update_date = models.DateField(auto_now_add=True, verbose_name="更新日")
    ingre_numbers = models.IntegerField(verbose_name="数量")
    ingre_unit = models.CharField(max_length=50, choices=UNIT, verbose_name="単位")
    expiration_date = models.ForeignKey(
        IngredientsModel, 
        null=True, 
        on_delete=models.PROTECT, 
        verbose_name="賞味期限",
        related_name='history_ing_exp_date',
    )
    def __str___(self):
        return f"{self.pk}/{self.ingre_name}"
    # IngredientsModelとリレーションを組みましょう。

class InfomationModel(models.Model):
    title = models.CharField(max_length=50,verbose_name="タイトル")
    text = models.TextField(max_length=1000,verbose_name="メモ")
    date = models.DateField(auto_now_add=True)
    refrigerator = models.ForeignKey(
        RefrigeratorModel, 
        on_delete=models.PROTECT,
        verbose_name="冷蔵庫名"
    )
    def __str__(self):
        return self.title

# Below here, these are additonal Models.

class SalesInfoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    refrigerator = models.ForeignKey(RefrigeratorModel, on_delete=models.PROTECT)

class TodaysRecipeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    ingredients = models.ForeignKey(IngredientsModel, on_delete=models.PROTECT)