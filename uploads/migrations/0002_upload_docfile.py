# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-01 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='docFile',
            field=models.FileField(default='settings.MEDIA_ROOT/dbms.pdf', upload_to=b''),
        ),
    ]
