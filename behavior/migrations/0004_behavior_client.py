# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160104_0242'),
        ('behavior', '0003_behavior_is_positive'),
    ]

    operations = [
        migrations.AddField(
            model_name='behavior',
            name='client',
            field=models.ManyToManyField(to='profiles.Client'),
        ),
    ]
