# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squiz', '0002_auto_20160301_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizinstance',
            name='current_question',
            field=models.CharField(default='1,2', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quizinstance',
            name='state',
            field=models.CharField(default='joinable', max_length=32, choices=[(b'joinable', b'joinable'), (b'inprogress', b'inprogress'), (b'over', b'over')]),
            preserve_default=False,
        ),
    ]
