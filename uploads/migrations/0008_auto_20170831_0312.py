# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-30 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0007_auto_20170831_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='description',
            field=models.CharField(default=None, max_length=300),
        ),
    ]
