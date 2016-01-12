# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0004_auto_20160104_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caregiver',
            old_name='is_staff',
            new_name='is_admin',
        ),
    ]
