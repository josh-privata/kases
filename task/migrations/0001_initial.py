# Generated by Django 2.0.3 on 2018-12-01 01:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalTaskCategory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Category')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task Category',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTaskClassification',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Classification')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task Classification',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTaskPriority',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Priority')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task Priority',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTaskStatus',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Status')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task Status',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTaskStatusGroup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Status Group')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task Status Group',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalTaskType',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Type')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Task Type',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='TaskCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Category')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
            ],
            options={
                'verbose_name': 'Task Category',
                'verbose_name_plural': 'Task Categories',
            },
        ),
        migrations.CreateModel(
            name='TaskClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Classification')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
            ],
            options={
                'verbose_name': 'Task Classification',
                'verbose_name_plural': 'Task Classifications',
            },
        ),
        migrations.CreateModel(
            name='TaskPriority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Priority')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
            ],
            options={
                'verbose_name': 'Task Priority',
                'verbose_name_plural': 'Task Priorities',
            },
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Status')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
            ],
            options={
                'verbose_name': 'Task Status',
                'verbose_name_plural': 'Task Status',
            },
        ),
        migrations.CreateModel(
            name='TaskStatusGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Status Group')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
                ('status', models.ManyToManyField(blank=True, to='task.TaskStatus', verbose_name='Task Status')),
            ],
            options={
                'verbose_name': 'Task Status Group',
                'verbose_name_plural': 'Task Status Groups',
            },
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('title', models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Type')),
                ('colour', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Colour')),
            ],
            options={
                'verbose_name': 'Task Type',
                'verbose_name_plural': 'Task Types',
            },
        ),
    ]
