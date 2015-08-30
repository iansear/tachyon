# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20150816_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='claim_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='drop_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='pick_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]
