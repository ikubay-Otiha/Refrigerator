# Generated by Django 3.2.10 on 2022-02-06 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ref_app', '0005_auto_20220206_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='compartmentmodel',
            name='refrigerator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='ref_app.refrigeratormodel'),
            preserve_default=False,
        ),
    ]
