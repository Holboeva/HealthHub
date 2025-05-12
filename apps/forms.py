from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.forms import Form, CharField
from django.forms.models import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = 'username', 'email', 'password'

    def clean_password(self):
        password = self.cleaned_data.get('password')
        hash_p = make_password(password)
        return hash_p

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(max_length=100)