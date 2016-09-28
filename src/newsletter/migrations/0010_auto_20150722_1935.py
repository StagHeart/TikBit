# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0009_auto_20150722_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagecounter',
            old_name='HomePage',
            new_name='home_page',
        ),
    ]
