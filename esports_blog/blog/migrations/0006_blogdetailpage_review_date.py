# Generated by Django 3.2.7 on 2021-09-26 10:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogdetailpage_handheld_console_blogdetailpage_mobile_blogdetailpage_pc_blogdetailpage_ps4_blogdetai'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailpage_review',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Post date'),
            preserve_default=False,
        ),
    ]
