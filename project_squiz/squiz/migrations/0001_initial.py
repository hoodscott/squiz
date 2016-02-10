# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=128)),
                ('answer', models.CharField(max_length=128)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionHasCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('this_category', models.ForeignKey(to='squiz.Category')),
                ('this_question', models.ForeignKey(to='squiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionInRound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('this_question', models.ForeignKey(to='squiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('quiz', models.ForeignKey(to='squiz.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='QuizTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=32, choices=[(b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thurssday'), (b'Friday', b'Friday'), (b'Saturday', b'Saturday'), (b'Sunday', b'Sunday')])),
                ('time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoundHasCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('this_category', models.ForeignKey(to='squiz.Category')),
                ('this_round', models.ForeignKey(to='squiz.Round')),
            ],
        ),
        migrations.CreateModel(
            name='RoundInQuiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('this_quiz', models.ForeignKey(to='squiz.Quiz')),
                ('this_round', models.ForeignKey(to='squiz.Round')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('time', models.ForeignKey(to='squiz.QuizTime')),
            ],
        ),
        migrations.AddField(
            model_name='questioninround',
            name='this_round',
            field=models.ForeignKey(to='squiz.Round'),
        ),
        migrations.AddField(
            model_name='player',
            name='quiz_instance',
            field=models.ForeignKey(to='squiz.QuizInstance'),
        ),
    ]
