# Generated by Django 4.2.6 on 2023-11-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_remove_usermodel_is_premium_usermodel_premium_till'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
