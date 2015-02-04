# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings
from unipath import Path

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('geolocation', models.CharField(max_length=150, blank=True)),
                ('link original', models.URLField()),
                ('attached', models.BooleanField(default=False)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=Path('./public/media'), null=True, verbose_name=b'image', blank=True)),
                ('liked_users', models.ManyToManyField(related_name='Liked_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
