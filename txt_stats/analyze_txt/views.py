from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AnalyzeTxt
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import TextInput
from .utils import *

import requests

from django.contrib.auth.models import User


# Create your views here.
class TextInputViews(viewsets.ModelViewSet):
    queryset = TextInput.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AnalyzeTextSerializer
        return TextInputSerializer


def home(response):
    if response.method == "POST":
        buff = "case_sensitive" in response.POST.keys()
        call = requests.post("http://127.0.0.1:8000/api/", data={"title": response.POST["title"],
                                                                 "text": response.POST["text"],
                                                                 "case_sensitive": buff})
        call = call.json()
        return redirect(f"/view/{call['id']}")

    f = AnalyzeTxt()
    return render(response, "analyze_txt/home.html", {"form": f})


def list_analyzed(response):
    call = requests.get("http://127.0.0.1:8000/api")
    return render(response, "analyze_txt/list_analyzed.html", {"texts": call.json()})


def analyzed(response, id):
    call = requests.get(f"http://127.0.0.1:8000/api/{id}")
    call = call.json()
    plot = plot_words(call["occurrences"])
    return render(response, "analyze_txt/analyzed.html", {"text": call["text"],
                                                          "words": call["occurrences"],
                                                          "plot": plot,
                                                          "palindromes": call["palindromes"]})
