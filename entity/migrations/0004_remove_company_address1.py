# Generated by Django 2.0.3 on 2018-12-01 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0003_auto_20181201_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='address1',
        ),
    ]