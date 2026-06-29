from django import forms

class AddNewForm(forms.Form):
    text = forms.CharField(label = "Text of new", widget = forms.Textarea(attrs = {"placeholder": "Hier schreiben", "class": "Text_new"}))
    name = forms.CharField(label = "Name of new", widget = forms.TextInput(attrs = {"placeholder": "Hier schreiben", "class": "Text_new"}))
    image = forms.ImageField(label = "Image of new", required= False, widget = forms.FileInput(attrs = {"placeholder": "Hier Bild einfügen", "class": "Image_new"}))


class LoginForm(forms.Form):
    username = forms.CharField(label = "Nickname", widget = forms.TextInput(attrs = {"placeholder": "Hier Nicknamen eingeben", "class": "Nickname_user"}))
    password = forms.CharField(label = "Passwort", widget = forms.PasswordInput(attrs = {"placeholder": "Hier Passwort eingeben", "class": "Password_user"}))

class RegisterForm (forms.Form):
    username = forms.CharField(label = "Nickname", widget = forms.TextInput(attrs = {"placeholder": "Hier Nicknamen eingeben", "class": "Nickname_user"}))
    password = forms.CharField(label = "Passwort", widget = forms.PasswordInput(attrs = {"placeholder": "Hier Passwort eingeben", "class": "Password_user"}))
    password2 = forms.CharField(label = "Passwort2", widget = forms.PasswordInput(attrs = {"placeholder": "Passwort erneut eingeben", "class": "Password_user"}))