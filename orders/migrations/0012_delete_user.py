# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20181206_1451'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
