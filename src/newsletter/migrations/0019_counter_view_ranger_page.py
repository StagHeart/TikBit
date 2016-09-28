# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0018_signup_ranger'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter_view',
            name='ranger_page',
            field=models.IntegerField(editable=False, default=0),
        ),
    ]
