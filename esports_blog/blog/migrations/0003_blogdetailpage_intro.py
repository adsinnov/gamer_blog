# Generated by Django 3.2.7 on 2021-09-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogdetailpage_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogdetailpage',
            name='intro',
            field=models.CharField(default='Introduction', help_text='overwrites the defaults title', max_length=100),
            preserve_default=False,
        ),
    ]