# Generated by Django 2.1 on 2019-09-21 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190921_2350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='photo',
            new_name='photo_1',
        ),
        migrations.AddField(
            model_name='posts',
            name='photo_2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='photo_3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='photo_4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='photo_5',
            field=models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='photo_6',
            field=models.ImageField(blank=True, default='', null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='posts',
            name='photo_main',
            field=models.ImageField(default='', upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
