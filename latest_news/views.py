from django.shortcuts import render
from django.views.generic import ListView

from latest_news.models import Forex, News


# Create your views here.

def index(request):
    currency = Forex.objects.all()
    news = News.objects.all()
    return render(request, template_name="index.html", context={"currency": currency, "news": news})


def our_team(request):
    return render(request, template_name="our_team.html", context={})


def new_detail(request, id):
    new = News.objects.get(id=id)
    return render(request, template_name="new_details.html", context={"new": new})