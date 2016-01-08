# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='behavior',
            name='antecedent_text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='behavior',
            name='consequence_text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='intervention',
            name='behavior',
            field=models.ManyToManyField(to='behavior.Behavior'),
        ),
    ]
