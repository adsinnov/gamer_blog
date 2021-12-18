import os
from django.shortcuts import render
from wagtail.core.models import Page
from wagtail.search.models import Query
from django.views.generic import TemplateView

env = os.environ.copy()


class RobotsView(TemplateView):

    content_type = 'text/plain'

    def get_template_names(self):
        return 'robots.txt'




def search(request):
    # Search
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search_query.html', {
        'search_query': search_query,
        'search_results': search_results,
    })