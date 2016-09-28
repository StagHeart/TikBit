# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_signup_squiggles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUp_Squiggles',
            new_name='SignUpSquiggles',
        ),
    ]
