# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-26 07:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_auto_20170226_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 26, 12, 34, 46, 487943)),
        ),
    ]
