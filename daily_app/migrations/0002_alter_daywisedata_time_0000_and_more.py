# Generated by Django 5.0.6 on 2024-07-03 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daywisedata',
            name='time_0000',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_0200',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_0400',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_0800',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_1000',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_1200',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_1400',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_1600',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_1800',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_2000',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='daywisedata',
            name='time_2200',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]