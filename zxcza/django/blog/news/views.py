from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article
from django.template import loader

# Create your views here.
def articles(request):
    template = loader.get_template('index.html')
    context = {
        'articles': Article,
    }
    return HttpResponse(template.render(context, request))
    