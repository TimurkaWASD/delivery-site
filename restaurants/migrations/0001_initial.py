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
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('image', models.ImageField(upload_to='images/categories/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('size', models.IntegerField(verbose_name='Размер')),
                ('image', models.ImageField(upload_to='images/products/', verbose_name='Фото')),
                ('is_sale', models.BooleanField(default=False, verbose_name='Акция')),
                ('discount', models.IntegerField(verbose_name='Скидка %')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('address', models.TextField(verbose_name='Адрес')),
                ('rating', models.IntegerField(verbose_name='Рейтинг')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/restaurants', verbose_name='Фото')),
                ('is_work', models.BooleanField(default=False, verbose_name='Работает')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.city', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Рестораны',
            },
        ),
    ]
