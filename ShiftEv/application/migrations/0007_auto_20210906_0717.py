# Generated by Django 3.2.6 on 2021-09-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_alter_vehicledata_car_type_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicledata',
            name='color_id',
        ),
        migrations.AddField(
            model_name='vehicledata',
            name='color_id',
            field=models.ManyToManyField(to='application.VehicleColor'),
        ),
    ]