# Generated by Django 3.2.6 on 2021-09-03 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_alter_vehicledata_color_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledata',
            name='car_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_type', to='application.cartype'),
        ),
    ]
