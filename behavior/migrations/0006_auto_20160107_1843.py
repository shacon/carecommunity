# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0005_auto_20160104_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='behavior',
            name='client',
        ),
        migrations.AlterField(
            model_name='behavior',
            name='is_positive',
            field=models.BooleanField(),
        ),
        migrations.AddField(
            model_name='behavior',
            name='client',
            field=models.ForeignKey(to='profiles.Client'),
        ),
    ]
