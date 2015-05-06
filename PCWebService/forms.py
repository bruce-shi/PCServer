__author__ = 'lovew_000'
from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    username = forms.CharField(label="User name",required=True)
    email = forms.EmailField(label="Email Address",required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)
    password_conf = forms.CharField(widget=forms.PasswordInput,required=True)

    def clean(self):
        form_data = self.cleaned_data
        password = form_data.get("password",None)
        password_conf = form_data.get("password_conf",None)
        if password is None:
            self._errors["password"] = ["Password is empty"]
        elif password_conf is None:
            self._errors["password_conf"] = ["Password Confirm is empty"]
        elif form_data.get('password') != form_data.get('password_conf'):
            self._errors["password"] = ["Password do not match"]
            del form_data['password']
        return form_data


    def clean_email(self):
        email = self.cleaned_data.get("email",None)
        if email:
            if User.objects.filter(email=email).exists():
                self._errors['email'] = ["Email address already registered"]
        return email


    def clean_username(self):
        username = self.cleaned_data.get("username",None)
        if username:
            if User.objects.filter(username=username).exists():
                self._errors['username'] = ["username already registered"]
        return username
