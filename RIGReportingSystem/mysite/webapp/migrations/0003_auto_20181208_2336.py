# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-12-08 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_researchgrant_rm_grant'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='rig',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='webapp.RIG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='rig',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='webapp.RIG'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='researchgrant',
            name='rig',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='webapp.RIG'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='performance',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
    ]
