# Generated by Django 4.0.3 on 2022-03-16 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0019_rename_ingredientshistory_ingredientshistorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientshistorymodel',
            name='ingre',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='ref_app.ingredientsmodel'),
            preserve_default=False,
        ),
    ]