# Generated by Django 2.2.6 on 2019-10-17 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0011_auto_20191017_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 6, 1, 49, 609371)),
        ),
    ]
