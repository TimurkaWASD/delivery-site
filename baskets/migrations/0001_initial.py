# Generated by Django 5.0.3 on 2024-03-15 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='Сумма')),
                ('status', models.SmallIntegerField(choices=[(1, 'Заказ создан'), (2, 'Заказ обрабатывается'), (3, 'Заказ завершен'), (4, 'Заказ отменен')], default=1, verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
            },
        ),
        migrations.CreateModel(
            name='Basket_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='Сумма')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baskets.basket', verbose_name='Корзина')),
            ],
            options={
                'verbose_name': 'Продукт из корзины',
                'verbose_name_plural': 'Продукты из корзины',
            },
        ),
    ]
