# Generated by Django 2.2 on 2019-04-23 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_api', '0004_auto_20190422_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='lended_to',
        ),
    ]
