# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0012_pagecounter_about_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecounter',
            old_name='app_page',
            new_name='apps_page',
        ),
        migrations.RenameField(
            model_name='pagecounter',
            old_name='game_page',
            new_name='games_page',
        ),
    ]
