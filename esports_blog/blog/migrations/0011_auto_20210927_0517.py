# Generated by Django 3.2.7 on 2021-09-27 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210927_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hand_held_console_details',
            name='customised_title',
        ),
        migrations.RemoveField(
            model_name='mobile_details',
            name='customised_title',
        ),
        migrations.RemoveField(
            model_name='pc_details',
            name='customised_title',
        ),
        migrations.RemoveField(
            model_name='ps4_details',
            name='customised_title',
        ),
        migrations.RemoveField(
            model_name='review_details',
            name='customised_title',
        ),
        migrations.RemoveField(
            model_name='xbox_details',
            name='customised_title',
        ),
    ]
