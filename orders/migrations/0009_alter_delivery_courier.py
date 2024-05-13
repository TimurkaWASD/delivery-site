# Generated by Django 5.0.3 on 2024-04-02 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0003_alter_courier_photo'),
        ('orders', '0008_delete_paymentmethod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='courier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='couriers.courier', verbose_name='Курьер'),
        ),
    ]
