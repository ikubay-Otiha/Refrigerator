# Generated by Django 3.2.10 on 2022-02-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ref_app", "0002_refrigeratormodel_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="IngredientsModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("numbers", models.IntegerField()),
                (
                    "unit",
                    models.CharField(
                        choices=[("ko", "個"), ("fukuro", "袋"), ("hon", "本")],
                        max_length=50,
                    ),
                ),
            ],
        ),
    ]
