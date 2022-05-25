from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.forms import ModelForm, Form

from accounts.models import CustomUser


class CustomUserCreationForm1(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'user_type')


class CustomUserCreationForm(Form):
    email = forms.EmailField()
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    password_confirmation = forms.CharField(widget=forms.PasswordInput(), validators=[validate_password])
    classroom = forms.CharField()