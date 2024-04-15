# Generated by Django 5.0.4 on 2024-04-15 09:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("routes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="routes",
            name="travel_time",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]