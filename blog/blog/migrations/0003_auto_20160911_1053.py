# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-11 02:53
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160911_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
    ]