# Generated by Django 3.2.6 on 2021-10-20 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0067_auto_20211020_0621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vs_vehicles',
            name='brand_nl',
        ),
        migrations.RemoveField(
            model_name='vs_vehicles',
            name='model_nl',
        ),
    ]
