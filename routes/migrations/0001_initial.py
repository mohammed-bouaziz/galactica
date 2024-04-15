# Generated by Django 5.0.4 on 2024-04-15 09:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Routes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("origin", models.CharField(max_length=128)),
                ("destination", models.CharField(max_length=128)),
                ("travel_time", models.IntegerField()),
            ],
        ),
    ]
