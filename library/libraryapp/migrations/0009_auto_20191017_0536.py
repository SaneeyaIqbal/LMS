# Generated by Django 2.2.6 on 2019-10-17 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0008_auto_20191017_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 5, 36, 18, 596056)),
        ),
    ]
