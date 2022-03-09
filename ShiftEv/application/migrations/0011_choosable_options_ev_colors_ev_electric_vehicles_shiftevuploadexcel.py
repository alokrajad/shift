# Generated by Django 3.2.6 on 2021-09-29 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0010_auto_20210906_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='electric_vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_en', models.CharField(max_length=200)),
                ('model_en', models.CharField(max_length=200)),
                ('brand_nl', models.CharField(max_length=200)),
                ('model_nl', models.CharField(max_length=200)),
                ('version', models.CharField(max_length=200)),
                ('description_en', models.TextField(blank=True, null=True)),
                ('description_nl', models.TextField(blank=True, null=True)),
                ('wtlp_range', models.IntegerField()),
                ('additional_percentage', models.IntegerField()),
                ('battery_capacity', models.IntegerField()),
                ('tax_value', models.FloatField()),
                ('expected_delivery_time', models.IntegerField(blank=True, null=True)),
                ('category', models.IntegerField()),
                ('car_type', models.CharField(choices=[('Standard', 'Standard_Car'), ('Best', 'Best_Buys')], max_length=10)),
                ('ispublished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftEvUploadExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ev_file', models.FileField(blank=True, null=True, upload_to='excel')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='colors_ev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(blank=True, max_length=200, null=True)),
                ('hex_code', models.CharField(blank=True, max_length=20, null=True)),
                ('r', models.CharField(blank=True, max_length=5, null=True)),
                ('g', models.CharField(blank=True, max_length=5, null=True)),
                ('b', models.CharField(blank=True, max_length=5, null=True)),
                ('img1', models.ImageField(blank=True, null=True, upload_to='images')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='images')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='images')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='images')),
                ('img5', models.ImageField(blank=True, null=True, upload_to='images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vehicledata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='application.electric_vehicles')),
            ],
        ),
        migrations.CreateModel(
            name='choosable_options_ev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('option_name_nl', models.CharField(blank=True, max_length=200, null=True)),
                ('option_value', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('vehicledata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choosableoptions', to='application.electric_vehicles')),
            ],
        ),
    ]
