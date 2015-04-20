# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RSSCrawler', '0002_auto_20150419_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsssourcelist',
            name='last_hash',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
