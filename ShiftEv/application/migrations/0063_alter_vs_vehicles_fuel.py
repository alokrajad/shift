# Generated by Django 3.2.6 on 2021-10-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0062_auto_20211013_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vs_vehicles',
            name='fuel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
