# Generated by Django 2.2.5 on 2021-05-30 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210530_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='date_completed',
            new_name='datecompleted',
        ),
    ]
