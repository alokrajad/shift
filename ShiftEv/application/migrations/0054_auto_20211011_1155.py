# Generated by Django 3.2.6 on 2021-10-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0053_electric_vehicles_long_range_vehicles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors_ev',
            name='img1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img3',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img4',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img5',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]