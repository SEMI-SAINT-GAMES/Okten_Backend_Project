# Generated by Django 4.2.6 on 2023-11-13 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_usermodel_is_premium'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='is_premium',
        ),
    ]
