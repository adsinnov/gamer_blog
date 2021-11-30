from wagtail.core import blocks

class TitleAndText(blocks.StructBlock):
    title = blocks.CharBlock(required=True,help_text="Add the Title Here")
    text =  blocks.CharBlock(required=True,help_text="Add the Title Here")

class Meta:
    template = "streams/title_and_text_block.html"
    icon = "edit"
    lable = "Title and Text"