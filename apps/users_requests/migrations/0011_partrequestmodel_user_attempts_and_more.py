# Generated by Django 4.2.6 on 2023-11-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_requests', '0010_alter_partrequestmodel_car_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='partrequestmodel',
            name='user_attempts',
            field=models.IntegerField(default=3),
        )
    ]
