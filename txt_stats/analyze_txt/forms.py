from django import forms


class CreateTxtForm(forms.Form):
    title = forms.CharField(label="title", max_length=2000)
    text = forms.CharField(widget=forms.Textarea(), label="text", initial="Enter text", min_length=1, max_length=1e6)
    case_sensitive = forms.BooleanField(label="Case_sensitive", required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    email = forms.CharField(label="email", max_length=100)
    password = forms.CharField(label="password", max_length=50, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=20)
    password = forms.CharField(label="password", max_length=50, widget=forms.PasswordInput())


class ChangePasswordForm(forms.Form):
    password = forms.CharField(label="Confirm password", max_length=50, widget=forms.PasswordInput())
    new_password = forms.CharField(label="New password", max_length=50, widget=forms.PasswordInput())
