# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-10 07:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hexdata',
            name='machine_id',
        ),
    ]