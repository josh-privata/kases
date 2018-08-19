# Generated by Django 2.0.3 on 2018-07-28 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0009_auto_20180729_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casedevice',
            name='case',
        ),
        migrations.RemoveField(
            model_name='casedevice',
            name='device_ptr',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='authorisation',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='case',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='category',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='classification',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='device_ptr',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='manufacturer',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='rep',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='resposible_party',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='service_contract',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='status',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='type',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='warranty_responsible',
        ),
        migrations.RemoveField(
            model_name='historicalcasedevice',
            name='warranty_vendor',
        ),
        migrations.RenameField(
            model_name='caseinventory',
            old_name='decription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='historicalcaseinventory',
            old_name='decription',
            new_name='description',
        ),
        migrations.DeleteModel(
            name='CaseDevice',
        ),
        migrations.DeleteModel(
            name='HistoricalCaseDevice',
        ),
    ]