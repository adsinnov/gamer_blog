# Generated by Django 3.2.7 on 2021-10-21 17:30

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211021_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagemeta',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]