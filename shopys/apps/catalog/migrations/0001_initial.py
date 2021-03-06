# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 05:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品类型')),
                ('slug', models.SlugField(help_text='根据name生成的，用于生成界面url，必须唯一', unique=True, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='描述')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否激活')),
                ('meta_keywords', models.CharField(help_text='关键字输入区域', max_length=255, verbose_name='meta 关键字')),
                ('meta_description', models.CharField(help_text='关键字输入区域', max_length=255, verbose_name='meta 关键字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'db_table': 'categories',
                'verbose_name_plural': '产品类型',
                'ordering': ['-create_time'],
                'verbose_name': '产品类型',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='产品名称')),
                ('slug', models.SlugField(help_text='根据name生成的，用于生成界面url，必须唯一', max_length=255, unique=True, verbose_name='Slug')),
                ('brand', models.CharField(max_length=50, verbose_name='品牌')),
                ('sku', models.CharField(max_length=50, verbose_name='计量单位')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='价格')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, verbose_name='旧价格')),
                ('image', models.ImageField(max_length=50, upload_to='', verbose_name='图片')),
                ('is_active', models.BooleanField(default=True, verbose_name='设为激活')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='标为畅销')),
                ('is_featured', models.BooleanField(default=False, verbose_name='标为推荐')),
                ('quantity', models.IntegerField(default=1, verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(help_text='关键字输入区域', max_length=255, verbose_name='Meta 关键词')),
                ('meta_description', models.CharField(help_text='关键字输入区域', max_length=255, verbose_name='meta 关键字')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'db_table': 'products',
                'verbose_name_plural': '产品名称',
                'ordering': ['-create_time'],
                'verbose_name': '产品名称',
            },
        ),
    ]
