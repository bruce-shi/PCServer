# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PCCore', '0002_words'),
        ('PCWebService', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cachenews',
            name='keywords',
            field=models.ManyToManyField(to='PCCore.KeyWords'),
        ),
        migrations.AddField(
            model_name='cachenews',
            name='static_url',
            field=models.URLField(default='http://localhost'),
            preserve_default=False,
        ),
    ]
