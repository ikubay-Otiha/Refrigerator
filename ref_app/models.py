from django.db import models

# Create your models here.

CATEGORY = (('refrigerator_room','冷蔵室'),('Freezing_room','冷凍室'),('child_room','チルド室'),('vegetable_room','野菜室'))
class RefrigeratorModel(models.Model):
    doorname = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length = 50,
        choices = CATEGORY
    )
    def __str__(self):
        return self.doorname

UNIT = (('ko','個'),('fukuro','袋'),('hon','本'),('gram','g'),
        ('kilogram','kg'),('milliliter','ml'),('liter','L'))
class IngredientsModel(models.Model):
    name = models.CharField(max_length=200)
    numbers = models.IntegerField()
    unit = models.CharField(
        max_length = 50,
        choices = UNIT
    )
    def __str__(self):
        return self.name

