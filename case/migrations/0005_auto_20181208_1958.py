# Generated by Django 2.0.3 on 2018-12-08 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_auto_20181208_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casetask',
            name='title',
            field=models.CharField(help_text='Enter a title for the Task', max_length=128, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='historicalcasetask',
            name='title',
            field=models.CharField(help_text='Enter a title for the Task', max_length=128, verbose_name='Title'),
        ),
    ]
