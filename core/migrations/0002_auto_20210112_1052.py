# Generated by Django 3.1.5 on 2021-01-12 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'managed': True, 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'managed': True, 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'managed': True, 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='slug',
        ),
    ]
