# Generated by Django 2.2.6 on 2019-11-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20191112_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemslist',
            name='release_year',
            field=models.IntegerField(),
        ),
    ]
