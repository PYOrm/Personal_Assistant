from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, template_name="index.html", context={})


def our_team(request):
    return render(request, template_name="our_team.html", context={})
