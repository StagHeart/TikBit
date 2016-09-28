# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0015_auto_20150723_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUpCounter',
            new_name='Counter_SignUp',
        ),
        migrations.RenameModel(
            old_name='ViewCounter',
            new_name='Counter_View',
        ),
    ]
