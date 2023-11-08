# Generated by Django 4.2.6 on 2023-10-29 01:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('car_brand', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\d]{2,30}$', 'not valid')])),
                ('car_model', models.CharField(max_length=30)),
                ('part_name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[A-Z][a-zA-Z\\d]{2,30}$', 'not valid')])),
                ('vin', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('\\b[(A-H|J-N|P|R-Z|0-9)]{17}\\b', 'OEM must be 17 symbols')])),
                ('oem', models.CharField(max_length=40)),
                ('about', models.CharField(max_length=10000)),
                ('engine_volume', models.FloatField(validators=[django.core.validators.MinValueValidator(0.2), django.core.validators.MaxValueValidator(10.0)])),
            ],
            options={
                'db_table': 'part_requests',
            },
        ),
    ]