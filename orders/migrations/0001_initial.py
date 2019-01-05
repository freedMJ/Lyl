# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('usertoken', models.CharField(max_length=40)),
                ('orderno', models.CharField(unique=True, max_length=40)),
                ('orderamount', models.DecimalField(max_digits=65535, decimal_places=65535)),
                ('created_at', models.BigIntegerField(blank=True, null=True)),
                ('is_filled', models.IntegerField(blank=True, null=True)),
                ('service_type', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
    ]
