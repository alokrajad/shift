# Generated by Django 3.2.6 on 2021-10-03 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_alter_shiftevuploadexcel_ev_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shiftevuploadexcel',
            name='ev_file',
            field=models.FileField(blank=True, default=None, upload_to='excel', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['ods', 'xls', 'xlsx', 'xlsm', 'xlsb'])]),
        ),
    ]
