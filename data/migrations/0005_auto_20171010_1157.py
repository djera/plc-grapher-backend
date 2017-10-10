# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-10 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20171010_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='variableconfig',
            name='endBit',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='variableconfig',
            name='endByte',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='variableconfig',
            name='startBit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variableconfig',
            name='startByte',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variableconfig',
            name='type',
            field=models.CharField(choices=[('bool', 'Boolean'), ('integer', 'Int'), ('double', 'DInt'), ('byte', 'Byte')], default='default', max_length=50),
            preserve_default=False,
        ),
    ]