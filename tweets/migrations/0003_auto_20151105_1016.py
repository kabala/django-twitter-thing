# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_hashtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='country',
            field=models.CharField(verbose_name='país', max_length=30),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(verbose_name='tweet', max_length=160),
        ),
    ]
