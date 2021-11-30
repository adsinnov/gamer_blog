from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.core.paginator import Page
from django.db import models
from wagtail.admin import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from Stream import content_blocks


class Review_Lists(Page):
    template = "blog/Review_list.html"
    custom_title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),

    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = Review_Details.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["Review"] = posts
        return context


class PS4_Lists(Page):
    template = "blog/PS4_list.html"
    custom_title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),

    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = PS4_Details.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["PS4"] = posts
        return context


class XBOX_Lists(Page):
    template = "blog/XBOX_list.html"
    custom_title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),

    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = XBOX_Details.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["Xbox"] = posts
        return context


class PC_Lists(Page):
    template = "blog/PC_list.html"
    custom_title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),

    ]
    verbose_name = "PC Category Page"

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = PC_Details.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["PC"] = posts
        return context


class Hand_Held_Console_Lists(Page):
    template = "blog/HHC_list.html"
    custom_title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),

    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = Hand_Held_Console_Details.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["HHC"] = posts
        return context


class Mobile_Lists(Page):
    template = "blog/Mobile_list.html"
    custom_title = models.CharField(max_length=128, blank=False, null=False, help_text='overwrites the defaults '
                                                                                       'title')
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),

    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = Mobile_Details.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["Mobile"] = posts
        return context


class Review_Details(Page):
    template = "blog/blog_detail_page.html"

    intro = models.CharField(max_length=100, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    author = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    quote = models.CharField(max_length=100, blank=True, null=True, help_text='overwrites the defaults '
                                                                              'title')
    date = models.DateField("Post date")

    categories = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                    'title', default="Reviews")

    keywords = models.CharField(max_length=100, blank=False, null=True, help_text='Keywords')

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = Mobile_Details.objects.live().public().order_by('-first_published_at')

        context["review_posts"] = all_posts
        return context

    Featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("simple_richtext", blocks.RichTextBlock()),
            ("Blog_image", content_blocks.Image_block()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("categories"),
        FieldPanel("intro"),
        ImageChooserPanel("Featured_image"),
        StreamFieldPanel("content"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('quote'),
        ImageChooserPanel("author_image"),
        FieldPanel('keywords'),
    ]


class PS4_Details(Page):
    template = "blog/blog_detail_page.html"

    intro = models.CharField(max_length=100, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    author = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    quote = models.CharField(max_length=100, blank=True, null=True, help_text='overwrites the defaults '
                                                                              'title')
    date = models.DateField("Post date")

    categories = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                    'title', default="PS4")

    keywords = models.CharField(max_length=100, blank=False, null=True, help_text='Keywords')

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = Review_Details.objects.live().public().order_by('-first_published_at')

        context["review_posts"] = all_posts
        return context

    Featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("simple_richtext", blocks.RichTextBlock()),
            ("Blog_image", content_blocks.Image_block()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("categories"),
        FieldPanel("intro"),
        ImageChooserPanel("Featured_image"),
        StreamFieldPanel("content"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('quote'),
        ImageChooserPanel("author_image"),
        FieldPanel('keywords'),
    ]


class XBOX_Details(Page):
    template = "blog/blog_detail_page.html"

    intro = models.CharField(max_length=100, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    author = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    quote = models.CharField(max_length=100, blank=True, null=True, help_text='overwrites the defaults '
                                                                              'title')
    date = models.DateField("Post date")

    categories = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                    'title', default="XBOX")
    keywords = models.CharField(max_length=100, blank=False, null=True, help_text='Keywords')

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = PS4_Details.objects.live().public().order_by('-first_published_at')

        context["review_posts"] = all_posts
        return context

    Featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("simple_richtext", blocks.RichTextBlock()),
            ("Blog_image", content_blocks.Image_block()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("categories"),
        FieldPanel("intro"),
        FieldPanel('keywords'),
        ImageChooserPanel("Featured_image"),
        StreamFieldPanel("content"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('quote'),

        ImageChooserPanel("author_image"),
    ]


class PC_Details(Page):
    template = "blog/blog_detail_page.html"

    intro = models.CharField(max_length=100, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    author = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    quote = models.CharField(max_length=100, blank=True, null=True, help_text='overwrites the defaults '
                                                                              'title')
    date = models.DateField("Post date")

    categories = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                    'title', default="PC")

    keywords = models.CharField(max_length=100, blank=False, null=True, help_text='Keywords')

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = XBOX_Details.objects.live().public().order_by('-first_published_at')

        context["review_posts"] = all_posts
        return context

    Featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("simple_richtext", blocks.RichTextBlock()),
            ("Blog_image", content_blocks.Image_block()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("categories"),
        FieldPanel("intro"),
        FieldPanel('keywords'),
        ImageChooserPanel("Featured_image"),
        StreamFieldPanel("content"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('quote'),
        ImageChooserPanel("author_image"),
    ]


class Hand_Held_Console_Details(Page):
    template = "blog/blog_detail_page.html"

    intro = models.CharField(max_length=100, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    author = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    quote = models.CharField(max_length=100, blank=True, null=True, help_text='overwrites the defaults '
                                                                              'title')
    date = models.DateField("Post date")

    categories = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                    'title',
                                  default="Hand Held Console")
    keywords = models.CharField(max_length=100, blank=False, null=True, help_text='Keywords')

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = PC_Details.objects.live().public().order_by('-first_published_at')

        context["review_posts"] = all_posts
        return context

    Featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("simple_richtext", blocks.RichTextBlock()),
            ("Blog_image", content_blocks.Image_block()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("categories"),
        FieldPanel("intro"),
        FieldPanel('keywords'),
        ImageChooserPanel("Featured_image"),
        StreamFieldPanel("content"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('quote'),
        ImageChooserPanel("author_image"),
    ]


class Mobile_Details(Page):
    template = "blog/blog_detail_page.html"

    intro = models.CharField(max_length=100, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    author = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                'title')
    quote = models.CharField(max_length=100, blank=True, null=True, help_text='overwrites the defaults '
                                                                              'title')
    date = models.DateField("Post date")

    categories = models.CharField(max_length=50, blank=False, null=False, help_text='overwrites the defaults '
                                                                                    'title', default="Mobile")
    keywords = models.CharField(max_length=100, blank=False, null=True, help_text='Keywords')

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = Hand_Held_Console_Details.objects.live().public().order_by('-first_published_at')

        context["review_posts"] = all_posts
        return context

    Featured_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    author_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )
    content = StreamField(
        [
            ("simple_richtext", blocks.RichTextBlock()),
            ("Blog_image", content_blocks.Image_block()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("categories"),
        FieldPanel("intro"),
        FieldPanel('keywords'),
        ImageChooserPanel("Featured_image"),
        StreamFieldPanel("content"),
        FieldPanel('date'),
        FieldPanel('author'),
        FieldPanel('quote'),
        ImageChooserPanel("author_image"),
    ]

    def save(self, *args , **kwargs):
        key = make_template_fragment_key(
            "detail_page_cache",
            [self.id],
        )
        cache.delete(key)

        return super().save(*args , **kwargs)
