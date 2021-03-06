# Generated by Django 3.2.6 on 2021-10-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0055_auto_20211012_0549'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarVsBasicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_en', models.CharField(max_length=200)),
                ('brand_nl', models.CharField(max_length=200)),
                ('model_en', models.CharField(max_length=200)),
                ('model_nl', models.CharField(max_length=200)),
                ('color_en', models.CharField(blank=True, max_length=200, null=True)),
                ('color_nl', models.CharField(blank=True, max_length=200, null=True)),
                ('version', models.CharField(blank=True, max_length=200, null=True)),
                ('licence_plate', models.CharField(max_length=200, unique=True)),
                ('transition', models.CharField(blank=True, max_length=100, null=True)),
                ('pitch_en', models.TextField(default=None)),
                ('pitch_nl', models.TextField(default=None)),
                ('doors', models.IntegerField(blank=True, null=True)),
                ('category', models.IntegerField()),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('construction_year', models.IntegerField(blank=True, null=True)),
                ('fuel', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('trailer_hitch', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('navigation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('air_conditioning', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('tax_value', models.FloatField()),
                ('first_registration', models.IntegerField()),
                ('power_pk', models.IntegerField()),
                ('power_kw', models.IntegerField()),
                ('tax_addition', models.FloatField()),
                ('end_date', models.DateField()),
                ('images', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
