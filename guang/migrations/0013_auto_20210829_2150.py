# Generated by Django 3.2.6 on 2021-08-29 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guang', '0012_auto_20210829_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='value',
            name='col',
        ),
        migrations.AlterField(
            model_name='col',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 29, 21, 50, 53, 469488), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='table',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 29, 21, 50, 53, 464484), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='value',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 29, 21, 50, 53, 469488), verbose_name='更新时间'),
        ),
    ]
