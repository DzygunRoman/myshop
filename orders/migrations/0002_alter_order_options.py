# Generated by Django 4.2.9 on 2024-02-06 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
    ]
