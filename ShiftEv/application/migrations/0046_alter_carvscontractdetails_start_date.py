# Generated by Django 3.2.6 on 2021-10-09 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0045_carvsbasicdata_carvscontractdetails_carvsoptions_carvstaxdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carvscontractdetails',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]