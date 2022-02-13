# Generated by Django 3.2.10 on 2022-02-12 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ref_app', '0011_infomationmodel_refrigerator'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodaysRecipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ref_app.ingredientsmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refrigerator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ref_app.refrigeratormodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
