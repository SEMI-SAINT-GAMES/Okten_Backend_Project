# Generated by Django 4.2.6 on 2023-11-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_requests', '0005_currencymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencymodel',
            name='buy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='currencymodel',
            name='sale',
            field=models.FloatField(),
        ),
    ]
