from django.shortcuts import render
from django.http import HttpResponse
from .models import News

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
