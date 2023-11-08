# Generated by Django 4.2.6 on 2023-10-30 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_usermodel_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.profilemodel'),
        ),
    ]