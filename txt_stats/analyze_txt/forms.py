from django import forms


class AnalyzeTxt(forms.Form):
    txt = forms.CharField(label="", initial="Enter text you want to analyze", min_length=1, max_length=1e6)

