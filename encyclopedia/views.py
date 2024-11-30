from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound

from . import util
import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    if util.get_entry(title):
        # convert markdown -> html
        return render(request, "encyclopedia/entry.html", {"title": title, "content": markdown.markdown(util.get_entry(title))})
    return HttpResponseNotFound(f"There is no content for {title}")
