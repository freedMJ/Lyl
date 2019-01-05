# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181204_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderno',
            field=models.CharField(unique=True, max_length=80),
        ),
    ]
