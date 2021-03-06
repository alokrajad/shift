# Generated by Django 3.2.6 on 2021-09-06 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20210906_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choosableoption',
            name='name_in_en',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='choosableoption',
            name='name_in_nl',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='choosableoption',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
