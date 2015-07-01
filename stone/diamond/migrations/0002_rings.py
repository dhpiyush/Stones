# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
