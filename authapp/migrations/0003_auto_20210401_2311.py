# Generated by Django 3.1.7 on 2021-04-01 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20210330_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 3, 20, 11, 16, 208885, tzinfo=utc)),
        ),
    ]
