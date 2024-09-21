# Generated by Django 4.0.3 on 2022-04-07 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ref_app", "0030_alter_ingredientshistorymodel_ingre_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="ingredientshistorymodel",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
