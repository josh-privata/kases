# Generated by Django 2.0.3 on 2019-05-04 00:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_auto_20190428_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 0, 19, 23, 509216, tzinfo=utc), help_text='Select a date for the Task', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='historicalcaseevent',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 0, 19, 23, 509216, tzinfo=utc), help_text='Select a date for the Task', verbose_name='Date'),
        ),
    ]
