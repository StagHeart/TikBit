# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0014_pagecounter_lab_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignUpCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('all_sign', models.IntegerField(editable=False, default=0)),
                ('squiggles_sign', models.IntegerField(editable=False, default=0)),
                ('herbs_sign', models.IntegerField(editable=False, default=0)),
                ('friends_sign', models.IntegerField(editable=False, default=0)),
                ('fitness_sign', models.IntegerField(editable=False, default=0)),
                ('goodnews_sign', models.IntegerField(editable=False, default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='PageCounter',
            new_name='ViewCounter',
        ),
    ]
