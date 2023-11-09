# Generated by Django 4.2.6 on 2023-11-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_requests', '0002_partrequestmodel_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='partrequestmodel',
            name='currency',
            field=models.CharField(choices=[('uah', 'UAH'), ('usd', 'USD'), ('eur', 'EUR')], default=1, max_length=3),
            preserve_default=False,
        ),
    ]
