# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0006_auto_20160107_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='behavior',
            name='antecedent_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='behavior',
            name='consequence_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='behavior',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='behavior',
            field=models.ForeignKey(to='behavior.Behavior'),
        ),
        migrations.AlterField(
            model_name='intervention',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
    ]
