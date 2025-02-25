# Generated by Django 5.0.3 on 2024-03-15 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baskets', '0001_initial'),
        ('couriers', '0001_initial'),
        ('customers', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_datetime', models.DateField(verbose_name='Дата оплаты')),
                ('payment_method', models.CharField(max_length=50, verbose_name='Метод оплаты')),
                ('status', models.SmallIntegerField(choices=[(1, 'Ожидание оплаты'), (2, 'Обработка платежа'), (3, 'Оплата прошла успешно'), (4, 'Оплата не удалась'), (5, 'Оплата возвращена'), (6, 'Оплата отменена'), (7, 'Оплата истекла'), (8, 'Ожидание верификации платежа'), (9, 'Не удалось верифицировать платеж'), (10, 'Платеж верифицирован')], default=1, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Метод оплаты',
                'verbose_name_plural': 'Методы оплат',
            },
        ),
        migrations.CreateModel(
            name='Review_orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_datetime', models.DateField(verbose_name='Время доставки')),
                ('status', models.SmallIntegerField(choices=[(1, 'Заказ приянт в обработку'), (2, 'Заказ собран и готов к отправке'), (3, 'Заказ передан курьеру'), (4, 'Заказ находится в пути к месту доставки'), (5, 'Заказ доставлен получателю'), (6, 'Заказ отклонен или отменен'), (7, 'Заказ возвращен на склад'), (8, 'Заказ доставлен, подтверждение получено')], default=1, verbose_name='Статус')),
                ('start_order_datetime', models.DateField(verbose_name='Время начала доставки')),
                ('end_order_datetime', models.DateField(verbose_name='Время окончания доставки')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='couriers.courier', verbose_name='Курьер')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_datetime', models.DateField(verbose_name='Время заказа')),
                ('total_amount', models.IntegerField(verbose_name='Общая сумма')),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baskets.basket', verbose_name='Корзина')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
