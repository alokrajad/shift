# Generated by Django 3.2.6 on 2021-09-30 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_choosable_options_ev_colors_ev_electric_vehicles_shiftevuploadexcel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colors_ev',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='colors_ev',
            name='img5',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
