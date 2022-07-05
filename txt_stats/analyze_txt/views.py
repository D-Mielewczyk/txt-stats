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

    # @staticmethod
    # def retrieve(request, pk=None):
    #     serializer = TextInputSerializer(txt)
    #     words = count_words(serializer.data["text"], serializer.data["case_sensitive"])
    #     palindromes = extract_palindromes(words)
    #     print(serializer.data)
    #     return Response({"Title": serializer.data["title"], "Occurances": words, "Palindromes": palindromes})


def home(response):
    if response.method == "POST":
        t = TextInputViews()
        return t.create(response.POST)
        # return redirect(response, "/db/")
    f = AnalyzeTxt()
    return render(response, "analyze_txt/home.html", {"form": f})


def analyzed(response, id):
    api = requests.get(f"http://127.0.0.1:8000/db/{id}")
    api = api.json()
    plot = plot_words(api["occurrences"])
    return render(response, "analyze_txt/analyzed_txt.html", {"text": api["text"],
                                                              "words": api["occurrences"],
                                                              "plot": plot,
                                                              "palindromes": api["palindromes"]})
