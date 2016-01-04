# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('behavior', '0002_auto_20160104_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=50)),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('problem_behaviors', models.ManyToManyField(related_name='+', to='behavior.Behavior')),
                ('strengths', models.ManyToManyField(related_name='+', to='behavior.Behavior')),
            ],
        ),
    ]
