# Generated by Django 2.2.7 on 2019-11-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0006_history_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='description',
        ),
    ]
