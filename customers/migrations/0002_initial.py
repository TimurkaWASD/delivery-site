# Generated by Django 5.0.3 on 2024-03-15 03:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='card',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='customer_address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='Клиент'),
        ),
    ]
