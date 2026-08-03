from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Schoolclasses, Customuser
from .forms import AddNewForm, LoginForm, RegisterForm, UserSettings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

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


def classinfos(request, classinfos_pk):
    classinfos = get_object_or_404(Schoolclasses, pk=classinfos_pk)
    context = {"classinfos": classinfos}
    return render(request, "main/classinfos.html", context)


def account(request):
    account = request.user
    message = ""
    if request.method == "POST":
        form = UserSettings(request.POST, request.FILES)
        if form.is_valid():
            try:
                name = form.cleaned_data["name"]
                text = form.cleaned_data["text"]
                try:
                    image = request.FILES ["image"]
                    News.objects.create(header = name, text = text, image = image).save()
                except Exception as e:
                    print(f"System Fehler: {e}")
                    News.objects.create(header = name, text = text).save()
                return redirect("homepage")
            except Exception as e:
                print(f"System Fehler: {e}")
                message = "Fehlgeschlagen"
        else:
            message = "Fehlgeschlagen"
    data = {"name_user": account.first_name, 
            "birthday_date_user": account.birthday_date, 
            "phone_user": account.phone_number, 
            "password_user": account.password, 
            "bio_user": account.biography}
    form = UserSettings(initial = data)
    context = {"account": account, "form": form}
    return render(request, "main/account.html", context, message)


def register(request):
    message = ""
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            try:
                user_obj = Customuser.objects.get(username = username)
                message = "Dieses Konto exestiert bereits"
            except Exception as e:
               if password == password2:
                   user = Customuser(username = username)
                   user.set_password(password)
                   user.save()
                   login(request, user)
                   return redirect("homepage")
               else:
                   message = "Passwörter müssen identisch sein"
    form = RegisterForm()
    context = {"form": form, "form_message": message}
    return render(request, "main/register.html", context)


def log_in(request):
    message = ""
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            try:
                user_obj = Customuser.objects.get(username = username)
                user_a = authenticate(username = username, password = password)
                if user_a is not None:
                    login(request, user_a)
                    return redirect("homepage")
                else:
                    message = "Passwort ist falsch"
            except Exception as e:
                message = "Dieses Konto exestiert nicht"
        else:
            message = "Etwas ist schiefgelaufen..."
    form = LoginForm()
    context = {"form": form, "form_message": message}
    return render(request, "main/log_in.html", context)


def log_out(request):
    logout(request)
    return redirect("homepage")



def add_new(request):
    message = ""
    if request.method == "POST":
        form = AddNewForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                name = form.cleaned_data["name"]
                text = form.cleaned_data["text"]
                try:
                    image = request.FILES ["image"]
                    News.objects.create(header = name, text = text, image = image).save()
                except Exception as e:
                    print(f"System Fehler: {e}")
                    News.objects.create(header = name, text = text).save()
                return redirect("homepage")
            except Exception as e:
                print(f"System Fehler: {e}")
                message = "Fehlgeschlagen"
        else:
            message = "Fehlgeschlagen"
    form = AddNewForm()
    context = {"form": form,"form_message": message}
    return render(request, "main/add_new.html", context)


# def test():
#     print("Test")
#     print("☺☻♥")