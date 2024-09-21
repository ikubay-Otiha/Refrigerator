# Generated by Django 3.2.10 on 2022-01-31 15:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RefrigeratorModel",
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
                ("doorname", models.CharField(max_length=100)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
