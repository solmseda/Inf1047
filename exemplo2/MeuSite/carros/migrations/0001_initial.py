# Generated by Django 4.2.4 on 2023-11-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MTCars",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("NAME", models.TextField()),
                ("MPG", models.FloatField()),
                ("CYL", models.IntegerField()),
                ("DISP", models.FloatField()),
                ("HP", models.IntegerField()),
                ("DRAT", models.FloatField()),
                ("WT", models.FloatField()),
                ("QSEC", models.FloatField()),
                ("VS", models.IntegerField()),
                ("AM", models.IntegerField()),
                ("GEAR", models.IntegerField()),
                ("CARB", models.IntegerField()),
            ],
        ),
    ]
