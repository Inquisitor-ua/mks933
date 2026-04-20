from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Schoolclasses

# Create your views here.
def homepage(request):
    news = News.objects.all()
    context = {"title": "Hauptseite", "header": "Tag der Hauptseite", "news": news}
    return render(request, "main/homepage.html", context)

def lesson_plan(request):
    context = {"title": "Stundenplan", "header": "Tag des Stundenplans"}
    return render(request, "main/lesson_plan.html", context)

def informations(request):
    context = {"title": "Infos", "header": "Anmeldung"}
    return render(request, "main/informations.html", context)

def news(request, news_pk):
    new = get_object_or_404(News, pk=news_pk)
    context = {"new": new}
    return render(request, "main/news.html", context)

def classes(request):
    classes = Schoolclasses.objects.all()
    context = {"title": "Hauptseite", "header": "Klassen", "classes": classes}
    return render(request, "main/classes.html", context)