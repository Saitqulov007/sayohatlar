# Generated by Django 5.0.6 on 2024-07-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
        ("tours", "0011_hotel_hotel_class"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="images",
            field=models.ManyToManyField(blank=True, to="main.image"),
        ),
    ]
