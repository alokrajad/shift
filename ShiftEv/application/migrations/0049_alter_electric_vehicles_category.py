# Generated by Django 3.2.6 on 2021-10-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0048_alter_carvscontractdetails_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electric_vehicles',
            name='category',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]