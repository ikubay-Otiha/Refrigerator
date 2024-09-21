# Generated by Django 5.1.1 on 2024-09-21 03:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ref_app", "0035_delete_salesinfomodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredientshistorymodel",
            name="ingre_unit",
            field=models.CharField(
                choices=[
                    ("ko", "個"),
                    ("fukuro", "袋"),
                    ("hon", "本"),
                    ("gram", "g"),
                    ("kilogram", "kg"),
                    ("milliliter", "ml"),
                    ("liter", "L"),
                    ("hiki", "匹"),
                ],
                max_length=50,
                verbose_name="単位",
            ),
        ),
        migrations.AlterField(
            model_name="ingredientsmodel",
            name="unit",
            field=models.CharField(
                choices=[
                    ("ko", "個"),
                    ("fukuro", "袋"),
                    ("hon", "本"),
                    ("gram", "g"),
                    ("kilogram", "kg"),
                    ("milliliter", "ml"),
                    ("liter", "L"),
                    ("hiki", "匹"),
                ],
                max_length=50,
                verbose_name="単位",
            ),
        ),
    ]
