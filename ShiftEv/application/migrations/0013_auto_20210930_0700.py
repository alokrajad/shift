# Generated by Django 3.2.6 on 2021-09-30 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20210930_0700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colors_ev',
            name='img1',
        ),
        migrations.RemoveField(
            model_name='colors_ev',
            name='img2',
        ),
        migrations.RemoveField(
            model_name='colors_ev',
            name='img3',
        ),
        migrations.RemoveField(
            model_name='colors_ev',
            name='img4',
        ),
        migrations.RemoveField(
            model_name='colors_ev',
            name='img5',
        ),
    ]
