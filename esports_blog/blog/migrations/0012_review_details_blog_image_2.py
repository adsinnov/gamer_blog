# Generated by Django 3.2.7 on 2021-09-27 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0011_auto_20210927_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_details',
            name='blog_image_2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
