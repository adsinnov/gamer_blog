from django.db import models
from wagtail.admin import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel


class Flex_Pages(Page):
    template = "Flex/Flex_Pages.html"

    Title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content = StreamField(
        [
            ("title_and_text", blocks.CharBlock("full_richtext", blocks.RichTextBlock())),
            ("simple_richtext", blocks.RichTextBlock()),
        ],
        null=True,
        blank=True,
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content_panels = Page.content_panels + [
        FieldPanel("Title"),
        StreamFieldPanel("content"),
        ImageChooserPanel("blog_image"),

    ]

