# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0016_auto_20150724_2216'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Counter_SignUp',
        ),
    ]
