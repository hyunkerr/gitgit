# Generated by Django 2.2.3 on 2019-07-31 10:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190731_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 31, 10, 12, 57, 148324, tzinfo=utc)),
        ),
    ]
