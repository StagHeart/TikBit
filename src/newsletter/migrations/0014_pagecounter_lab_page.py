# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0013_auto_20150722_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecounter',
            name='lab_page',
            field=models.IntegerField(editable=False, default=0),
        ),
    ]
