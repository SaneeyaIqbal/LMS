# Generated by Django 2.2.6 on 2019-10-17 07:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0024_auto_20191017_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 7, 18, 21, 677116)),
        ),
    ]