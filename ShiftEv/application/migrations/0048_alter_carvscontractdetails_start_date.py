# Generated by Django 3.2.6 on 2021-10-09 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0047_alter_carvscontractdetails_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carvscontractdetails',
            name='start_date',
            field=models.DateField(default=datetime.date(2021, 10, 9)),
        ),
    ]
