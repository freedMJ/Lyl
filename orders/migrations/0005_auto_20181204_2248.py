# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181204_2247'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': False},
        ),
    ]
