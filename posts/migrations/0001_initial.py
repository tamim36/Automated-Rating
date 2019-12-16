# Generated by Django 2.1 on 2019-12-16 13:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('scores', models.DecimalField(blank=True, decimal_places=1, default=None, max_digits=2, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authcomments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemsList_name', models.CharField(max_length=200)),
                ('item_summary', models.CharField(max_length=200)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('numcomment', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=5, null=True)),
            ],
            options={
                'verbose_name_plural': 'Items',
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_slug', models.SlugField(default=1)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posted', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('post_item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.ItemsList', verbose_name='Posts')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.AddField(
            model_name='itemslist',
            name='item_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='posts.PostCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='posts.Posts'),
        ),
    ]
