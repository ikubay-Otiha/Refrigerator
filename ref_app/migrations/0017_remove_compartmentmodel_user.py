# Generated by Django 3.2.10 on 2022-02-23 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0016_compartmentmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compartmentmodel',
            name='user',
        ),
    ]
