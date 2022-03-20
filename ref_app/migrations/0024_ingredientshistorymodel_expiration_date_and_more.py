# Generated by Django 4.0.3 on 2022-03-20 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0023_remove_ingredientshistorymodel_update_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientshistorymodel',
            name='expiration_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='history_ing_exp_date', to='ref_app.ingredientsmodel', verbose_name='賞味期限'),
        ),
        migrations.AddField(
            model_name='ingredientshistorymodel',
            name='ingre_cpmt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='history_ing_cpmt', to='ref_app.ingredientsmodel', verbose_name='冷蔵室名'),
        ),
        migrations.AlterField(
            model_name='ingredientshistorymodel',
            name='ingre_name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='history_ing_name', to='ref_app.ingredientsmodel', verbose_name='食材名'),
        ),
        migrations.AlterField(
            model_name='ingredientsmodel',
            name='compartment',
            field=models.ManyToManyField(related_name='ing_cpmt', to='ref_app.compartmentmodel'),
        ),
        migrations.AlterField(
            model_name='ingredientsmodel',
            name='expiration_date',
            field=models.DateField(verbose_name='賞味期限'),
        ),
    ]
