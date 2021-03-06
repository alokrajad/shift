# Generated by Django 3.2.6 on 2021-10-01 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0015_auto_20210930_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electric_vehicles',
            name='additional_percentage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electric_vehicles',
            name='brand_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='electric_vehicles',
            name='model_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='electric_vehicles',
            name='wtlp_range',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
