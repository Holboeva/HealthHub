from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, EmailField
from django.forms.forms import Form
from django.forms.models import ModelForm
from django.forms.widgets import PasswordInput

from apps.models import User
from django.contrib.auth.forms import UserCreationForm


# class RegisterForm(UserCreationForm):
#     first_name = forms.CharField(label="First Name", max_length=50)
#     last_name = forms.CharField(label="Last Name", max_length=50)
#     email = forms.EmailField(label="Email Address", help_text="Enter a valid email")
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
#     password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ("username", "email", "first_name", "last_name", "password1", "password2")
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#
#         if password1 != password2:
#             raise forms.ValidationError("Passwords do not match.")
#         return password2
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


class RegisterModelForm(ModelForm):
    password = CharField(widget=PasswordInput())
    password_confirm = CharField(widget=PasswordInput())
    sms = CharField(label='SMS Code')
    email = EmailField()

    class Meta:
        model = User
        fields = ['email', 'sms', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Invalid username or password.")

        self.user = user
        return cleaned_data


class EmailForm(Form):
    email = CharField(max_length=255)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        query = User.objects.filter(email=email).exists()
        if query:
            raise ValidationError(f'{email} exists')
        return email

# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'first_name', 'last_name', 'password2')
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#
#     def clean_password(self):
#         password = self.cleaned_data.get('password1', 'password2')
#         return make_password(password)


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#
#     def clean(self):
#         data = super().clean()
#         username = data.get("username")
#         password = data.get("password")
#         user = User.objects.filter(username=username).first()
#         if user:
#             authenticate(username=username, password=password)
#         self.user = user
#         return user
