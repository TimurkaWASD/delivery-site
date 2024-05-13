# Generated by Django 5.0.3 on 2024-04-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_delivery_delivery_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='end_order_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время окончания доставки'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='start_order_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время начала доставки'),
        ),
    ]
