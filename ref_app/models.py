from django.db import models


# Create your models here.

class RefrigeratorModel(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

COMPARTMENT = (('Refrigerator','冷蔵室'),('Freezer','冷凍室'),('Vegetable','野菜室'),('Chilled','チルド室'),('Icebox','アイスボックス'))
class CompartmentModel(models.Model):
    name = models.CharField(
        max_length = 100,
        choices = COMPARTMENT
    )
    refrigerator = models.ForeignKey(RefrigeratorModel, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name

UNIT = (('ko','個'),('fukuro','袋'),('hon','本'),('gram','g'),
        ('kilogram','kg'),('milliliter','ml'),('liter','L'))
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
    def __str__(self):
        return self.name

