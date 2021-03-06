# Generated by Django 2.0.3 on 2018-12-23 01:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0001_initial'),
        ('entity', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalUserCategory',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical User Category',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUserClassification',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical User Classification',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUserStatus',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical User Status',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUserStatusGroup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical User Status Group',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='HistoricalUserType',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical User Type',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, choices=[('1', 'Mr.'), ('2', 'Mrs.')], max_length=10, null=True, verbose_name='Prefix')),
                ('bio', models.TextField(blank=True, default=None, max_length=500, null=True, verbose_name='User Biography')),
                ('location', models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Current Location')),
                ('birth_date', models.DateField(blank=True, default=None, null=True, verbose_name='Birth Date')),
                ('nickname', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Nickname')),
                ('aliases', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Aliases')),
                ('suffix', models.CharField(blank=True, max_length=55, null=True, verbose_name='Suffix')),
                ('notes', models.TextField(blank=True, max_length=255, null=True, verbose_name='Notes')),
                ('created', models.DateTimeField(editable=False, verbose_name='Creation date and time')),
                ('modified', models.DateTimeField(editable=False, null=True, verbose_name='Modification date and time')),
                ('gender', models.CharField(blank=True, max_length=55, null=True, verbose_name='Gender')),
                ('anniversary', models.DateTimeField(blank=True, null=True, verbose_name='Anniversary')),
                ('height', models.CharField(blank=True, max_length=55, null=True, verbose_name='Height')),
                ('weight', models.CharField(blank=True, max_length=55, null=True, verbose_name='Weight')),
                ('age', models.CharField(blank=True, max_length=55, null=True, verbose_name='Age')),
                ('taxfile', models.CharField(blank=True, max_length=55, null=True, verbose_name='Tax File Number')),
                ('date_started', models.DateTimeField(blank=True, null=True, verbose_name='Date Started')),
                ('salary', models.CharField(blank=True, max_length=55, null=True, verbose_name='Salary')),
                ('job_title', models.CharField(blank=True, max_length=55, null=True, verbose_name='Job Title')),
                ('role', models.CharField(blank=True, max_length=55, null=True, verbose_name='Role')),
                ('slug_first', models.SlugField(blank=True, editable=False, null=True, verbose_name='First Name Slug')),
                ('slug_last', models.SlugField(blank=True, editable=False, null=True, verbose_name='Last Name Slug')),
                ('slug_middle', models.SlugField(blank=True, editable=False, null=True, verbose_name='Middle Name Slug')),
                ('address', models.ManyToManyField(to='entity.Address', verbose_name='Address')),
                ('authorisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='utils.Authorisation', verbose_name='Person Authorisation')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='UserCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'User Category',
                'verbose_name_plural': 'User Categories',
            },
        ),
        migrations.CreateModel(
            name='UserClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'User Classification',
                'verbose_name_plural': 'User Classifications',
            },
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'User Status',
                'verbose_name_plural': 'User Status',
            },
        ),
        migrations.CreateModel(
            name='UserStatusGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
                ('status', models.ManyToManyField(blank=True, to='user.UserStatus', verbose_name='User Status')),
            ],
            options={
                'verbose_name': 'User Status Group',
                'verbose_name_plural': 'User Status Groups',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='Enter a title', max_length=50, verbose_name='Title')),
                ('colour', models.CharField(blank=True, default=None, help_text='(Optional) Enter a Hexidecimal colour representation', max_length=7, null=True, verbose_name='Colour')),
                ('description', models.CharField(blank=True, default=None, help_text='(Optional) Enter a description', max_length=250, null=True, verbose_name='Description')),
                ('created', models.DateTimeField(editable=False, help_text='The creation date', verbose_name='Creation Date')),
                ('modified', models.DateTimeField(editable=False, help_text='The mdification date', null=True, verbose_name='Modification date')),
            ],
            options={
                'verbose_name': 'User Type',
                'verbose_name_plural': 'User Types',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserCategory', verbose_name='Person Category'),
        ),
        migrations.AddField(
            model_name='profile',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserClassification', verbose_name='Person Classification'),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.ManyToManyField(to='entity.Email', verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserStatus', verbose_name='Person Status'),
        ),
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.ManyToManyField(to='entity.Telephone', verbose_name='Telephone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.UserType', verbose_name='Person Type'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.ManyToManyField(to='entity.Website', verbose_name='Website'),
        ),
    ]
