# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caretaker', '0002_caregiver_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='caregiver',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
