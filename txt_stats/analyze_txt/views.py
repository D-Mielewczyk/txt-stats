from django.http import HttpResponse
from django.shortcuts import render
from .forms import AnalyzeTxt
import re


# Create your views here.
def home(response):
    if response.method == "POST":
        if response.POST.get("start"):
            txt = response.POST.get("txt").lower()
            txt = re.sub(r'[^a-z ]', '', txt)

            words = {}
            for word in txt.split():
                if word not in words.keys():
                    words[word] = 0
                words[word] += 1
            res = f"<p>{words}</p>"
            return render(response, "analyze_txt/home.html", {"form": res})

    f = AnalyzeTxt()
    return render(response, "analyze_txt/home.html", {"form": f})
