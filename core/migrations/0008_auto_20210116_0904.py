# Generated by Django 3.1.5 on 2021-01-16 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_service_male'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='male',
            field=models.BooleanField(default=False, verbose_name='мужской зал (по умолчанию женский)'),
        ),
    ]
