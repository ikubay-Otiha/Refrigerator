# Generated by Django 4.0.3 on 2022-03-31 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("ref_app", "0027_alter_ingredientshistorymodel_ingre_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredientshistorymodel",
            name="update_date",
        ),
        migrations.AddField(
            model_name="ingredientshistorymodel",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="作成日",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ingredientshistorymodel",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, verbose_name="更新日"),
        ),
    ]
