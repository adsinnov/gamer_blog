# Generated by Django 3.2.7 on 2021-09-26 09:25

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailimages', '0023_add_choose_permissions'),
        ('blog', '0003_blogdetailpage_intro'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogListingPage_Review',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='overwrites the defaults title', max_length=128)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogDetailPage_Review',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('customised_title', models.CharField(help_text='overwrites the defaults title', max_length=128)),
                ('subtitle', models.CharField(help_text='overwrites the defaults title', max_length=128)),
                ('intro', models.CharField(help_text='overwrites the defaults title', max_length=100)),
                ('content', wagtail.core.fields.StreamField([('title_and_text', wagtail.core.blocks.CharBlock('full_richtext', wagtail.core.blocks.RichTextBlock())), ('simple_richtext', wagtail.core.blocks.RichTextBlock())], blank=True, null=True)),
                ('blog_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
