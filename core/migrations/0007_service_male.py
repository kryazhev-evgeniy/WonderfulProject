# Generated by Django 3.1.5 on 2021-01-16 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210113_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='male',
            field=models.BooleanField(default=True, verbose_name='мужской зал (по умолчанию женский)'),
        ),
    ]
