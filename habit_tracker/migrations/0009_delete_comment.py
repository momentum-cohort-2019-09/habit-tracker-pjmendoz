# Generated by Django 2.2.7 on 2019-11-08 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habit_tracker', '0008_habit_observer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
