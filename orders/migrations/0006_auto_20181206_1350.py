# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20181204_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.DeleteModel(
            name='Hero',
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={'managed': True},
        ),
    ]
