# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_auto_20150722_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageCounter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mainPage', models.IntegerField()),
            ],
        ),
    ]
