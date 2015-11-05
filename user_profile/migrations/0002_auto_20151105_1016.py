# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, verbose_name='correo', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(unique=True, verbose_name='usuario', db_index=True, max_length=10),
        ),
    ]
