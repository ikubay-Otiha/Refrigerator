# Generated by Django 4.0.3 on 2022-04-02 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0028_remove_ingredientshistorymodel_update_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientshistorymodel',
            name='ingre_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='history_ing_name', to='ref_app.ingredientsmodel', verbose_name='食材名'),
        ),
    ]