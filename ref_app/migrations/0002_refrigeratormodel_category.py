# Generated by Django 3.2.10 on 2022-02-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ref_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="refrigeratormodel",
            name="category",
            field=models.CharField(
                choices=[
                    ("refrigerator_room", "冷蔵室"),
                    ("Freezing_room", "冷凍室"),
                    ("child_room", "チルド室"),
                    ("vegetable_room", "野菜室"),
                ],
                default=1,
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
