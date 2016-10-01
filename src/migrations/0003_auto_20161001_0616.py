# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_auto_20161001_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 6, 16, 26, 200172, tzinfo=utc)),
        ),
    ]
