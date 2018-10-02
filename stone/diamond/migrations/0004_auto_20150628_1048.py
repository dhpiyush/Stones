# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0003_auto_20150628_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='bangles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='rings',
            old_name='rings_url',
            new_name='url',
        ),
    ]
