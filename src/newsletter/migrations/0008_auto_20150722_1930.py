# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_pagecounter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecounter',
            name='mainPage',
            field=models.IntegerField(editable=False, default=0),
        ),
    ]
