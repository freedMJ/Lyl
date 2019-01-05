# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('sex', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'hero',
            },
        ),
        migrations.AlterModelOptions(
            name='orders',
            options={},
        ),
    ]
