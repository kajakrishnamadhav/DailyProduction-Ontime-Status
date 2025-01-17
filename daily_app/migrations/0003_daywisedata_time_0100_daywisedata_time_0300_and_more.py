# Generated by Django 5.0.4 on 2024-07-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_app', '0002_alter_daywisedata_time_0000_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='daywisedata',
            name='time_0100',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_0300',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_0500',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_0600',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_0700',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_0900',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_1100',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_1300',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_1500',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_1700',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_1900',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_2100',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='daywisedata',
            name='time_2300',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
