from django.db import models
from wagtail.core import blocks


# Create your models here.
from wagtail.images.blocks import ImageChooserBlock


class Image_block(blocks.StructBlock):

    blog_image = ImageChooserBlock(help_text='Image the automagically cropped to 786px by 552px')


    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Add Image"