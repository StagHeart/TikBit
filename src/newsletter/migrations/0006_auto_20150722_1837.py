# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_signupfitness_signupfriends_signupherbs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SignUpFitness',
            new_name='SignUp_Fitness',
        ),
        migrations.RenameModel(
            old_name='SignUpFriends',
            new_name='SignUp_Friends',
        ),
        migrations.RenameModel(
            old_name='SignUpGoodNews',
            new_name='SignUp_GoodNews',
        ),
        migrations.RenameModel(
            old_name='SignUpHerbs',
            new_name='SignUp_Herbs',
        ),
        migrations.RenameModel(
            old_name='SignUpSquiggles',
            new_name='SignUp_Squiggles',
        ),
    ]
