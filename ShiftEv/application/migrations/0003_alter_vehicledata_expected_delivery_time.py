# Generated by Django 3.2.6 on 2021-09-02 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20210902_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicledata',
            name='expected_delivery_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
