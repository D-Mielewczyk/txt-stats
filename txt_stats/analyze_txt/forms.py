from django import forms


class AnalyzeTxt(forms.Form):
    title = forms.CharField(label="Title", max_length=2000)
    text = forms.CharField(widget=forms.Textarea(), label="Text", initial="Enter text", min_length=1, max_length=1e6)
    case_sensitive = forms.BooleanField(label="Case sensitive", required=False)
