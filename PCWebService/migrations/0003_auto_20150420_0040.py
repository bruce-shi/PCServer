# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSSCrawler', '0003_rsssourcelist_last_hash'),
        ('PCWebService', '0002_auto_20150419_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachenews',
            name='parent_list',
            field=models.ForeignKey(default='', to='RSSCrawler.RSSSourceList'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cachenews',
            name='static_url',
            field=models.URLField(unique=True),
        ),
    ]
