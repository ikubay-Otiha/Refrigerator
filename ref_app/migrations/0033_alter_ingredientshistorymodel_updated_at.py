# Generated by Django 4.0.3 on 2022-04-17 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0032_remove_ingredientsmodel_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientshistorymodel',
            name='updated_at',
            field=models.DateTimeField(null=True, verbose_name='更新日'),
        ),
    ]
