# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comment', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Downvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateField(null=True)),
                ('counter', models.IntegerField(default=0, null=True)),
                ('comment', models.ForeignKey(to='discussionboard.Comment', null=True, related_name='comment_downvote')),
            ],
            options={
                'db_table': 'downvote',
            },
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateField(null=True)),
                ('idea', models.TextField(max_length=200)),
                ('comment', models.ForeignKey(to='discussionboard.Comment', related_name='comment_idea')),
            ],
            options={
                'db_table': 'idea',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('topic', models.TextField(max_length=70)),
                ('description', models.TextField(max_length=250)),
                ('category', models.TextField(max_length=30)),
                ('counter', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'topic',
            },
        ),
        migrations.CreateModel(
            name='Upvote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('counter', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateField(null=True)),
                ('total', models.IntegerField(null=True)),
                ('comment', models.ForeignKey(to='discussionboard.Comment', null=True, related_name='comment_upvote')),
            ],
            options={
                'db_table': 'upvote',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.TextField(max_length=20, null=True)),
                ('last_name', models.TextField(max_length=20, null=True)),
                ('email', models.TextField(max_length=20, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('password', models.TextField(max_length=20, null=True)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='upvote',
            name='user',
            field=models.ForeignKey(to='discussionboard.User', null=True, related_name='upvote_user'),
        ),
        migrations.AddField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(to='discussionboard.User', related_name='topic_user'),
        ),
        migrations.AddField(
            model_name='idea',
            name='user',
            field=models.ForeignKey(to='discussionboard.User', related_name='idea_user'),
        ),
        migrations.AddField(
            model_name='downvote',
            name='user',
            field=models.ForeignKey(to='discussionboard.User', null=True, related_name='downvote_user'),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(to='discussionboard.Topic', related_name='comment_topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='discussionboard.User', related_name='comment_user'),
        ),
    ]
