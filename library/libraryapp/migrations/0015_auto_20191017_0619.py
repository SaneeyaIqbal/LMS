# Generated by Django 2.2.6 on 2019-10-17 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0014_auto_20191017_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='time',
            field=models.TextField(default=datetime.datetime(2019, 10, 17, 6, 19, 17, 312682)),
        ),
    ]
