# Generated by Django 5.0.3 on 2024-03-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('status', models.SmallIntegerField(choices=[(1, 'Доступен для назначения заказа'), (2, 'В пути к получению заказу'), (3, 'Получил заказ'), (4, 'В пути к месту доставки'), (5, 'Завершил доставку'), (6, 'Не работает'), (7, 'Работает')], default=1, verbose_name='Статус')),
                ('photo', models.ImageField(upload_to='images/courier', verbose_name='Аватар')),
            ],
            options={
                'verbose_name': 'Курьер',
                'verbose_name_plural': 'Курьеры',
            },
        ),
    ]
