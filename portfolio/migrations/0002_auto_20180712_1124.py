# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-12 08:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brian',
            options={'ordering': ['first_name']},
        ),
    ]
