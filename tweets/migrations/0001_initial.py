# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=160)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='user_profile.User')),
            ],
        ),
    ]
