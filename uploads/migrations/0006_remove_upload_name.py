# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_upload_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='name',
        ),
    ]