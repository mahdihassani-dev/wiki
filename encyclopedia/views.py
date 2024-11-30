from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import util
import markdown


def index(request):
    search = request.GET.get('q', '')
    head = 'All Pages' if search == '' else f'Search Result for "{search}"'
    
    entries = util.list_entries(search)
    for entry in entries:
        if search.lower() == entry.lower():
            return HttpResponseRedirect(reverse('entry', args=[search])) # redirect to entry of that content

    return render(request, "encyclopedia/index.html", {"entries": entries, "head": head})


def entry(request, title):
    if util.get_entry(title):
        # convert markdown -> html
        return render(request, "encyclopedia/entry.html", {"title": title, "content": markdown.markdown(util.get_entry(title))})
    return HttpResponseNotFound(f"There is no content for {title}")


