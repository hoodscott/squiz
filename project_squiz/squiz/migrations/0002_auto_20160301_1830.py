# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('squiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(to='squiz.Host'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='creator',
            field=models.ForeignKey(to='squiz.Host'),
        ),
        migrations.AlterField(
            model_name='quizinstance',
            name='host',
            field=models.ForeignKey(to='squiz.Host'),
        ),
        migrations.AlterField(
            model_name='round',
            name='creator',
            field=models.ForeignKey(to='squiz.Host'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='host',
            field=models.ForeignKey(to='squiz.Host'),
        ),
    ]
