# Generated by Django 4.2.6 on 2023-11-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_requests', '0008_alter_partrequestmodel_body_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partrequestmodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
