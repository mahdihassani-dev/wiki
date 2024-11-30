from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

from . import util
import markdown


def index(request):
    
    search = request.GET.get('q', '')
    head = 'All Pages' if search == '' else f'Search Result for "{search}"'

    return render(request, "encyclopedia/index.html", {"entries": util.list_entries(search), "head": head})


def entry(request, title):
    if util.get_entry(title):
        # convert markdown -> html
        return render(request, "encyclopedia/entry.html", {"title": title, "content": markdown.markdown(util.get_entry(title))})
    return HttpResponseNotFound(f"There is no content for {title}")
