# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-08 04:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDate',
        ),
        migrations.AddField(
            model_name='usersession',
            name='t_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
