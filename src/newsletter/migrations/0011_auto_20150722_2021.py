# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0010_auto_20150722_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagecounter',
            name='app_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='business_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='contact_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='fitness_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='friends_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='game_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='goodnews_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='herbs_page',
            field=models.IntegerField(editable=False, default=0),
        ),
        migrations.AddField(
            model_name='pagecounter',
            name='squiggles_page',
            field=models.IntegerField(editable=False, default=0),
        ),
    ]
