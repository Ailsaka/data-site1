# Generated by Django 3.2.6 on 2021-09-08 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guang', '0014_auto_20210829_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='tables_under_tag',
            field=models.IntegerField(default=0, verbose_name='当前表数量'),
        ),
        migrations.AlterField(
            model_name='col',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 14, 12, 8, 464722), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='table',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 14, 12, 8, 459718), verbose_name='更新时间'),
        ),
        migrations.AlterField(
            model_name='value',
            name='update',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 14, 12, 8, 464722), verbose_name='更新时间'),
        ),
    ]
