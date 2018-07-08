# Generated by Django 2.0.3 on 2018-07-01 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('evidence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Evidence Title')),
                ('reference', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Evidence Reference')),
                ('comment', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Comment')),
                ('bag_number', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Bag Number')),
                ('location', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Physical Location')),
                ('uri', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='File Location')),
                ('current_status', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Current Status')),
                ('qr_code_text', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='QR Code Text')),
                ('qr_code', models.BooleanField(default=False, verbose_name='QR Code')),
                ('retention_reminder_sent', models.BooleanField(default=False, verbose_name='Retention Reminder')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Evidence Slug')),
                ('retention_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Retention Date')),
                ('date_added', models.DateTimeField(auto_now=True, null=True, verbose_name='Date Added')),
                ('deadline', models.DateTimeField(auto_now=True, null=True, verbose_name='Deadline')),
                ('retention_start_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Retention Start Date')),
                ('assigned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evidence_assigned_by', to=settings.AUTH_USER_MODEL, verbose_name='Assigned By')),
                ('assigned_to', models.ManyToManyField(blank=True, related_name='evidence_assigned_to', to=settings.AUTH_USER_MODEL, verbose_name='Assigned To')),
                ('authorisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.EvidenceAuthorisation', verbose_name='Evidence Authorisation')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.EvidenceCategory', verbose_name='Evidence Category')),
                ('chain_of_custody', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evidence_chain_of_custody', to='evidence.ChainOfCustody', verbose_name='Chain Of Custody')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.EvidenceClassification', verbose_name='Evidence Classification')),
                ('custodian', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evidence_custodian', to=settings.AUTH_USER_MODEL, verbose_name='Custodian')),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.EvidencePriority', verbose_name='Evidence Priority')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.EvidenceStatus', verbose_name='Evidence Status')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evidence.EvidenceType', verbose_name='Evidence Type')),
            ],
            options={
                'verbose_name': 'Evidence',
                'verbose_name_plural': 'Evidence',
            },
        ),
        migrations.CreateModel(
            name='HistoricalEvidence',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Evidence Title')),
                ('reference', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Evidence Reference')),
                ('comment', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Comment')),
                ('bag_number', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Bag Number')),
                ('location', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Physical Location')),
                ('uri', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='File Location')),
                ('current_status', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Current Status')),
                ('qr_code_text', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='QR Code Text')),
                ('qr_code', models.BooleanField(default=False, verbose_name='QR Code')),
                ('retention_reminder_sent', models.BooleanField(default=False, verbose_name='Retention Reminder')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Evidence Slug')),
                ('retention_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Retention Date')),
                ('date_added', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Date Added')),
                ('deadline', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Deadline')),
                ('retention_start_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Retention Start Date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('assigned_by', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('authorisation', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.EvidenceAuthorisation')),
                ('category', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.EvidenceCategory')),
                ('chain_of_custody', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.ChainOfCustody')),
                ('classification', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.EvidenceClassification')),
                ('custodian', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('priority', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.EvidencePriority')),
                ('status', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.EvidenceStatus')),
                ('type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='evidence.EvidenceType')),
            ],
            options={
                'verbose_name': 'historical Evidence',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
    ]