# Generated by Django 3.2.6 on 2021-10-20 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0063_alter_vs_vehicles_fuel'),
    ]

    operations = [
        migrations.AddField(
            model_name='vs_vehicles',
            name='brand',
            field=models.CharField(default='abcd', max_length=200),
        ),
        migrations.AddField(
            model_name='vs_vehicles',
            name='model',
            field=models.CharField(default='abcd', max_length=200),
        ),
    ]