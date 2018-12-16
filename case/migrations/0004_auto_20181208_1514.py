# Generated by Django 2.0.3 on 2018-12-08 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_auto_20181208_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseevidence',
            name='note',
            field=models.ManyToManyField(blank=True, help_text='(Optional) Enter a note relating to the Evidence', related_name='evidence_note', to='utils.Note', verbose_name='Note'),
        ),
    ]
