# Generated by Django 4.2.6 on 2023-11-09 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_requests', '0006_alter_currencymodel_buy_alter_currencymodel_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partrequestmodel',
            name='region_of_car',
            field=models.CharField(choices=[('АР Крим', 'arkrym'), ('Вінницька', 'vinnytska'), ('Волинська', 'volynska'), ('Дніпропетровська', 'dnipropetrovska'), ('Донецька', 'donetska'), ('Житомирська', 'zhytomyrska'), ('Закарпатська', 'zakarpatska'), ('Івано-Франківська', 'ivano-frankivska'), ('Київська', 'kyivska'), ('Кіровоградська', 'kirovohradska'), ('Луганська', 'luhanska'), ('Львівська', 'lvivska'), ('Миколаївська', 'mykolaivska'), ('Одеська', 'odeska'), ('Полтавська', 'poltavska'), ('Рівненська', 'rivnenska'), ('Сумська', 'sumska'), ('Тернопільська', 'ternopilska'), ('Харківська', 'kharkivska'), ('Херсонська', 'khersonska'), ('Хмельницька', 'khmelnytska'), ('Черкаська', 'cherkaska'), ('Чернівецька', 'chernivetska'), ('Чернігівська', 'chernihivska')], max_length=20),
        ),
    ]
