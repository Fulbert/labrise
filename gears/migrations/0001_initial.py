# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Wing',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('wing_type', models.CharField(max_length=1, choices=[('P', 'Paraglider'), ('H', 'Hang glider'), ('O', 'Other')])),
                ('name', models.CharField(max_length=50)),
                ('area_flat', models.FloatField()),
                ('area_proj', models.FloatField()),
                ('span_flat', models.FloatField()),
                ('span_proj', models.FloatField()),
                ('aspect_ratio_flat', models.FloatField()),
                ('aspect_ratio_proj', models.FloatField()),
                ('cells', models.FloatField()),
                ('total_line_length', models.FloatField()),
                ('total_lines', models.FloatField()),
                ('line_diameters', models.CharField(max_length=50)),
                ('weight', models.FloatField()),
                ('v_trim', models.FloatField()),
                ('v_max', models.FloatField()),
                ('en_category', models.CharField(max_length=50)),
                ('takeoff_weight', models.FloatField()),
                ('year', models.DateField()),
                ('brand', models.ForeignKey(to='gears.Brand')),
                ('designers', models.ManyToManyField(to='gears.Designer')),
                ('pictures', models.ManyToManyField(to='gallery.Picture')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='brand',
            name='designers',
            field=models.ManyToManyField(to='gears.Designer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='brand',
            name='logo',
            field=models.ForeignKey(to='gallery.Picture'),
            preserve_default=True,
        ),
    ]
