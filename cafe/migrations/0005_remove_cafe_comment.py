# Generated by Django 2.0.1 on 2018-01-26 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_merge_20180126_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='comment',
        ),
    ]
