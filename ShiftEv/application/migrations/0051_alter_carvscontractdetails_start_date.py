# Generated by Django 3.2.6 on 2021-10-11 03:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0050_auto_20211010_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carvscontractdetails',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 10, 11)),
        ),
    ]
