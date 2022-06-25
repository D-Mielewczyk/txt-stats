from django import forms


class AnalyzeTxt(forms.Form):
    text = forms.CharField(label=None, initial="Enter text", min_length=1, max_length=1e6)
    case_sensitive = forms.BooleanField(label="Case sensitive")
