# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squiz', '0003_auto_20160316_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='answer',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
