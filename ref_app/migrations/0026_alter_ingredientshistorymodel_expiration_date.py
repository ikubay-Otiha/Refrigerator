# Generated by Django 4.0.3 on 2022-03-22 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0025_alter_compartmentmodel_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientshistorymodel',
            name='expiration_date',
            field=models.DateField(null=True, verbose_name='賞味期限'),
        ),
    ]
