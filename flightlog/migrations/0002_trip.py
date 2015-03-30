# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('space', '0001_initial'),
        ('flightlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('landing', models.ManyToManyField(to='space.Point', related_name='landing_list')),
                ('pilots', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('takeoff', models.ManyToManyField(to='space.Point', related_name='takeoff_list')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
