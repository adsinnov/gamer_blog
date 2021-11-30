from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from blog.models import Review_Details, Mobile_Details, PS4_Details, XBOX_Details, PC_Details, Hand_Held_Console_Details



class HomePage(Page):
    templates = "templates/home/home_page.html"
    max_count = 1
    banner_title = models.CharField(max_length=128, blank=False, null=False)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["Review"] = Review_Details.objects.live().public().order_by('-first_published_at')
        context["PS4"] = PS4_Details.objects.live().public().order_by('-first_published_at')
        context["Xbox"] = XBOX_Details.objects.live().public().order_by('-first_published_at')
        context["PC"] = PC_Details.objects.live().public().order_by('-first_published_at')
        context["HHC"] = Hand_Held_Console_Details.objects.live().public().order_by('-first_published_at')
        context["Mobile"] = Mobile_Details.objects.live().public().order_by('-first_published_at')
        return context

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")

    ]

    def save(self, *args , **kwargs):
        key = make_template_fragment_key(
            "home_page_cache",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args , **kwargs)