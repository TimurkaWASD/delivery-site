# Generated by Django 5.0.3 on 2024-04-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_payment_method_payment_method_payment_methods'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='payment_method',
            name='payment_methods',
            field=models.IntegerField(choices=[(1, 'Кредитная карта'), (2, 'Наличная оплата')], verbose_name='Метод оплаты'),
        ),
    ]
