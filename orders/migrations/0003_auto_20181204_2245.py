# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20181204_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='age',
        ),
        migrations.AlterField(
            model_name='hero',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='hero',
            name='sex',
            field=models.CharField(max_length=80),
        ),
    ]
