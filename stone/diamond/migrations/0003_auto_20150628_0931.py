# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0002_rings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rings',
            old_name='url',
            new_name='rings_url',
        ),
    ]
