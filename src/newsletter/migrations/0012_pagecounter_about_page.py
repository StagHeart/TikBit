# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0011_auto_20150722_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecounter',
            name='about_page',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
