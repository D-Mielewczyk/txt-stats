from django.http import HttpResponse
from django.shortcuts import render
from .forms import AnalyzeTxt
from re import sub
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextInputSerializer
from .models import TextInput
from .utils import *


# Create your views here.
class TextInputViews(APIView):
    @staticmethod
    def post(request):
        serializer = TextInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request, id=None):
        if id:
            item = TextInput.objects.get(id=id)
            words = count_words(item.text, item.case_sensitive)
            palindromes = get_palindromes(words)
            plot = plot_words(words)
            return render(request, "analyze_txt/analyzed_txt.html", {"input": item, "words": words, "palindromes": palindromes, "plot": plot})

        items = TextInput.objects.all()
        serializer = TextInputSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


def home(response):
    # if response.method == "POST":
    #     if response.POST.get("start"):
    #         txt = response.POST.get("text")
    #
    #         # TODO: redirect to site with results
    #         return render(response, "analyze_txt/home.html", {"form": res})

    f = AnalyzeTxt()
    return render(response, "analyze_txt/home.html", {"form": f})
