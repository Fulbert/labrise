# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gears', '0001_initial'),
        ('space', '0001_initial'),
        ('gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('takeoff_date', models.DateField()),
                ('landing_date', models.DateField()),
                ('description', models.TextField()),
                ('story', models.TextField()),
                ('is_public', models.BooleanField(default=True)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
                ('pilot', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('filename', models.FileField(upload_to='')),
                ('is_GPS', models.BooleanField(default=False)),
                ('landing_point', models.ForeignKey(related_name='landing_point', to='space.Point')),
                ('takeoff_point', models.ForeignKey(related_name='takeoff_point', to='space.Point')),
                ('waypoints', models.ManyToManyField(related_name='waypoints', to='space.Point')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='log',
            name='track',
            field=models.ForeignKey(to='flightlog.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='log',
            name='wing',
            field=models.ForeignKey(to='gears.Wing'),
            preserve_default=True,
        ),
    ]
