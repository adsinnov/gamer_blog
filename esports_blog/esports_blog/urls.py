from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
from django.views import defaults as default_views
from search import views as search_views

import esports_blog.views


urlpatterns = [
    path('robots.txt/',esports_blog.views.RobotsView.as_view(), name='robots'),
    path('sitemap.xml/', sitemap),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('404/', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
    path('500/', default_views.server_error),
    path('search/', search_views.search, name='search'),
    path('', include('pwa.urls')),

]


if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # path('__debug__/', include(debug_toolbar.urls)),


    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
