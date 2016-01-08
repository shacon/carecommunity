# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160104_0242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='client',
            new_name='caregiver',
        ),
    ]
