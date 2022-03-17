# Generated by Django 4.0.3 on 2022-03-15 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ref_app', '0017_remove_compartmentmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_date', models.DateField(auto_now_add=True, verbose_name='更新日')),
                ('ingre_name', models.CharField(max_length=200, verbose_name='食材名')),
                ('ingre_numbers', models.IntegerField(verbose_name='数量')),
                ('ingre_unit', models.CharField(choices=[('ko', '個'), ('fukuro', '袋'), ('hon', '本'), ('gram', 'g'), ('kilogram', 'kg'), ('milliliter', 'ml'), ('liter', 'L')], max_length=50, verbose_name='単位')),
                ('update_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='更新者')),
            ],
        ),
    ]