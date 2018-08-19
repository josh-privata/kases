# Generated by Django 2.0.3 on 2018-07-27 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0017_auto_20180727_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug_first',
            field=models.SlugField(blank=True, editable=False, null=True, verbose_name='First Name Slug'),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug_last',
            field=models.SlugField(blank=True, editable=False, null=True, verbose_name='Last Name Slug'),
        ),
        migrations.AlterField(
            model_name='person',
            name='slug_middle',
            field=models.SlugField(blank=True, editable=False, null=True, verbose_name='Middle Name Slug'),
        ),
    ]