# Generated by Django 3.2.6 on 2021-10-05 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0030_electric_vehicles_long_range_vehicles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='electric_vehicles',
            name='long_range_vehicles',
        ),
    ]
