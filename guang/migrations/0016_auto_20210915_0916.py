# Generated by Django 3.2.6 on 2021-09-15 09:16

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guang', '0015_auto_20210908_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='c0',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='列的数量'),
        ),
        migrations.AlterField(
            model_name='table',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 15, 9, 16, 20, 254607), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='value',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 15, 9, 16, 20, 259612), verbose_name='更新时间'),
        ),
        migrations.DeleteModel(
            name='Col',
        ),
    ]
