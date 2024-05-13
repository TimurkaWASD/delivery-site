# Generated by Django 5.0.3 on 2024-03-26 07:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baskets', '0002_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket_product',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.products', verbose_name='Блюдо'),
        ),
    ]
