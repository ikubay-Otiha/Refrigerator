# Generated by Django 3.2.10 on 2022-02-16 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ref_app', '0014_auto_20220214_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientsmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
