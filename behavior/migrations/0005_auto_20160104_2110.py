# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0004_behavior_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='behavior',
            name='second_field',
        ),
        migrations.RemoveField(
            model_name='intervention',
            name='behavior',
        ),
        migrations.AddField(
            model_name='intervention',
            name='behavior',
            field=models.ForeignKey(blank=True, to='behavior.Behavior', null=True),
        ),
    ]
