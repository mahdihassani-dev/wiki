from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import util
from .forms import NewPageForm, EditPageForm
import markdown
import random


def index(request):
    search = request.GET.get('q', '')
    head = 'All Pages' if search == '' else f'Search Result for "{search}"'

    entries = util.list_entries(search)
    for entry in entries:
        if search.lower() == entry.lower():
            # redirect to entry of that content
            return HttpResponseRedirect(reverse('entry', args=[search]))

    return render(request, "encyclopedia/index.html", {"entries": entries, "head": head})


def entry(request, title):
    if util.get_entry(title):
        # convert markdown -> html
        return render(request, "encyclopedia/entry.html", {"title": title, "content": markdown.markdown(util.get_entry(title))})
    return HttpResponseNotFound(f"There is no content for {title}")


def random_entry(request):
    entries = util.list_entries()
    if entries:
        random_title = random.choice(entries)
        return redirect("entry", title=random_title)
    return HttpResponseNotFound("No entries available.")
    

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('entry', args=[title]))
        else:
            return render(request, 'encyclopedia/new_page.html', {"form": form})

    return render(request, "encyclopedia/new_page.html", {"form": NewPageForm()})


def edit_page(request, title):
    entry = util.get_entry(title)
    if entry:
        if request.method == "POST":
            form = EditPageForm(request.POST)
            if form.is_valid():
                content = form.cleaned_data["content"]
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('entry', args=[title]))
            else:
                return render(request, 'encyclopedia/new_page.html', {"form": form})
        return render(request, 'encyclopedia/edit_page.html', {"form": EditPageForm(initial={"content": entry, "title": title})})
                
    return HttpResponseNotFound(f"There is no content for {title}")
