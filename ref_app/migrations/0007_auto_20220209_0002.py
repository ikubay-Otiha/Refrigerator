# Generated by Django 3.2.10 on 2022-02-08 15:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ref_app', '0006_compartmentmodel_refrigerator'),
    ]

    operations = [
        migrations.AddField(
            model_name='refrigeratormodel',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='compartmentmodel',
            name='name',
            field=models.CharField(choices=[('Refrigerator', '冷蔵室'), ('Freezer', '冷凍室'), ('Vegetable', '野菜室'), ('Chilled', 'チルド室'), ('Icebox', 'アイスボックス')], max_length=100),
        ),
    ]
