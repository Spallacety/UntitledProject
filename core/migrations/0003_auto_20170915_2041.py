# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 23:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170915_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='end',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start',
        ),
    ]