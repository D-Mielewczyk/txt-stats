from django.http import HttpResponse
from django.shortcuts import render
from .forms import AnalyzeTxt
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextInputSerializer
from .models import TextInput
from .utils import *

import logging

from django.contrib.auth.models import User


# Create your views here.
class TextInputViews(viewsets.ModelViewSet):
    queryset = TextInput.objects.all()
    serializer_class = TextInputSerializer

    @staticmethod
    def retrieve(request, pk=None):
        queryset = TextInput.objects.all()
        txt = get_object_or_404(queryset, pk=pk)
        serializer = TextInputSerializer(txt)
        words = count_words(serializer.data["text"], serializer.data["case_sensitive"])
        palindromes = get_palindromes(words)
        print(serializer.data)
        return Response({"Title": serializer.data["title"], "Occurances": words, "Palindromes": palindromes})


def home(response):
    f = AnalyzeTxt()
    # logging.critical("siema")
    print(User.objects.all())
    return render(response, "analyze_txt/home.html", {"form": f})
