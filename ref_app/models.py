from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RefrigeratorModel(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True)
    date = models.DateField(auto_now_add=True)
    user = models.ManyToManyField(User)
    # compartment = CompartmentModel.refrigerator_set.all()
    def __str__(self):
        return self.name

COMPARTMENT = (
    ('Refrigerator','冷蔵室'),('Freezer','冷凍室'),('Vegetable','野菜室'),
    ('Chilled','チルド室'),('Icebox','アイスボックス')
)
class CompartmentModel(models.Model):
    name = models.CharField(
        max_length = 100,
        choices = COMPARTMENT,
    )
    refrigerator = models.ForeignKey(RefrigeratorModel, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.refrigerator.name}/{self.get_name_display()}"

UNIT = (
    ('ko','個'),('fukuro','袋'),('hon','本'),('gram','g'),
    ('kilogram','kg'),('milliliter','ml'),('liter','L')
)
class IngredientsModel(models.Model):
    name = models.CharField(max_length=200)
    compartment = models.ManyToManyField(CompartmentModel)
    # example_door = models.ForeignKey(CompartmentModel) 
    # 一対多の場合:食材が多になる、キーは多につける。
    numbers = models.IntegerField()
    unit = models.CharField(
        max_length = 50,
        choices = UNIT
    )
    expiration_date = models.DateField()
    def __str__(self):
        return self.name

class InfomationModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    refrigerator = models.ForeignKey(RefrigeratorModel, on_delete=models.PROTECT)
    def __str__(self):
        return self.title

# Below here, these are additonal Models.

class SalesInfoModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    refrigerator = models.ForeignKey(RefrigeratorModel, on_delete=models.PROTECT)

class TodaysRecipeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ingredients = models.ForeignKey(IngredientsModel, on_delete=models.PROTECT)