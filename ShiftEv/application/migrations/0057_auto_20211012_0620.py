# Generated by Django 3.2.6 on 2021-10-12 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0056_carvsbasicdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='carvsbasicdata',
            name='ispublished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carvsbasicdata',
            name='air_conditioning',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='carvsbasicdata',
            name='navigation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
        migrations.AlterField(
            model_name='carvsbasicdata',
            name='trailer_hitch',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10),
        ),
    ]
