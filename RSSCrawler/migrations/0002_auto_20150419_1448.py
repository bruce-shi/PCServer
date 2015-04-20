# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('RSSCrawler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsscategory',
            name='publisher',
            field=models.CharField(default='none', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rsssourcelist',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 19, 6, 48, 37, 400000, tzinfo=utc), auto_created=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rsscategory',
            name='name',
            field=models.CharField(unique=True, max_length=255),
        ),
        migrations.RemoveField(
            model_name='rsssourcelist',
            name='category',
        ),
        migrations.AddField(
            model_name='rsssourcelist',
            name='category',
            field=models.ForeignKey(default='', to='RSSCrawler.RSSCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rsssourcelist',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
