# Generated by Django 5.0.3 on 2024-03-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_datetime',
            field=models.DateTimeField(verbose_name='Время заказа'),
        ),
    ]
