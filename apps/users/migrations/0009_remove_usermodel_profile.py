# Generated by Django 4.2.6 on 2023-10-30 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profilemodel_age_alter_usermodel_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='profile',
        ),
    ]
