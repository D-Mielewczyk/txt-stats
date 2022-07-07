import requests
from django.conf import settings
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import viewsets

from .forms import CreateTxtForm, RegisterForm, LoginForm, ChangePasswordForm
from .serializers import *
from .utils import *


# Create your views here.
class TextInputViews(viewsets.ModelViewSet):
    queryset = TextInput.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AnalyzeTextSerializer
        return TextInputSerializer


def create(response):
    if response.method == "POST":
        buff = "case_sensitive" in response.POST.keys()
        if response.user.is_authenticated:
            user = response.user.pk
        else:
            user = None
        call = requests.post(f"{settings.SITE}api/", data={"title": response.POST["title"],
                                                           "text": response.POST["text"],
                                                           "case_sensitive": buff,
                                                           "owner": user})
        call = call.json()
        return redirect(f"/view/{call['id']}")

    f = CreateTxtForm()
    return render(response, "analyze_txt/form.html", {"title": "Analyze your text", "form": f})


def account(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            if "password" in response.POST.keys():
                user = authenticate(response, username=response.user.username, password=response.POST["password"])
                if user is not None:
                    return render(response, "analyze_txt/message.html", {"title": "Wrong password!",
                                                                         "button": "Try again..."})
                u = User.objects.get(username=response.user.username)
                u.set_password(response.POST["new_password"])
                u.save()
                return render(response, "analyze_txt/message.html", {"title": "Password changed successfully.",
                                                                     "button": "Proceed to your account..."})
            else:
                logout(response)
                return redirect("/account/")
        f = ChangePasswordForm()
        return render(response, "analyze_txt/account.html", {"form": f, "user": response.user})

    if response.method == "POST":
        # Check if we are registering or logging in
        if "email" in response.POST.keys():
            user = User.objects.create_user(response.POST["username"], response.POST["email"],
                                            response.POST["password"])
            print(user)
        else:
            user = authenticate(response, username=response.POST["username"], password=response.POST["password"])
            if user is not None:
                login(response, user)
                return render(response, "analyze_txt/message.html", {"title": "Successfully logged in!",
                                                                     "button": "Proceed to your account..."})
            else:
                return render(response, "analyze_txt/message.html",
                              {"title": "Unsuccessful log in attempt! User with same login already exists",
                               "button": "Try again..."})

    f = LoginForm()
    f2 = RegisterForm()
    return render(response, "analyze_txt/double_form.html",
                  {"title": "Login", "form": f, "title2": "Register", "form2": f2})


def list_analyzed(response):
    call = requests.get(f"{settings.SITE}api")
    call = call.json()
    pop_this = []
    for index, text in enumerate(call):
        if not can_access(response.user, text["owner"]):
            pop_this.append(index)
    for i, v in enumerate(pop_this):
        call.pop(v - i)

    return render(response, "analyze_txt/list_analyzed.html", {"texts": call})


def analyzed(response, id):
    call = requests.get(f"{settings.SITE}api/{id}")
    call = call.json()
    if not can_access(response.user, call["owner"]):
        return render(response, "analyze_txt/message.html", {"title": "You don't have access to this data",
                                                             "button": "Go back...",
                                                             "href": "../"})
    plot = plot_words(call["occurrences"])
    return render(response, "analyze_txt/analyzed.html", {"text": call["text"],
                                                          "words": call["occurrences"],
                                                          "plot": plot,
                                                          "palindromes": call["palindromes"]})
