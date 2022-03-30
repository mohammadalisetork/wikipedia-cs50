from cgitb import html
from django.shortcuts import render
import markdown as md

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def css(request):
    md.markdownFromFile(
    input='entries/CSS.md',
    output='encyclopedia/templates/encyclopedia/output.html',
    encoding='utf8'
    )
    return render(request , 'encyclopedia/output.html')

