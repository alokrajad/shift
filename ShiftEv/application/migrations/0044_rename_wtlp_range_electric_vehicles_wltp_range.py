# Generated by Django 3.2.6 on 2021-10-08 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0043_alter_electric_vehicles_battery_capacity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='electric_vehicles',
            old_name='wtlp_range',
            new_name='wltp_range',
        ),
    ]
