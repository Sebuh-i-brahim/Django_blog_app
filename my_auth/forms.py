
from django import forms 

from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username=forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id'   : 'username',
                'placeholder' : 'İsdifadəçi adı',
                'name' : 'username',
            }
        )
    )
    email=forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-control',
            'id' : 'email',
            'placeholder' : 'Email',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id' : 'password',
            'placeholder' : 'Parol',
        }
    ))
    confirm = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id' : 'confirm',
            'placeholder' : 'Təkrar Parol',
        }
    ))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class' : 'custom-control-input',
            'id' : 'remember_me',
            'value': 'True'
        }
    ))
    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
        remember_me = self.cleaned_data.get("remember_me")
        if password and confirm and password != confirm:
            raise forms.ValidationError('Təkrar parol Parola bərabər deyil')

        values = {
            "username" : username,
            "email"    : email,
            "password" : password,
            "remember_me": remember_me,
        }
        return values
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm', 'remember_me')
        widgets = {
            'password': forms.PasswordInput(),
            'confirm' : forms.PasswordInput(),
        }


class LoginForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control',
            'id'   : 'username',
            'placeholder' : 'İsdifadəçi adı',
            'name' : 'username',
        }
    ))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'id' : 'password',
            'placeholder' : 'Parol',
            'name' : 'password',
        }
    ))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        attrs={
            'class' : 'custom-control-input',
            'id' : 'remember_me',
            'value' : 'True'
        }
    ))
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        remember_me = self.cleaned_data.get("remember_me")
        values = {
            'username' : username,
            'password' : password,
            'remember_me' : remember_me,
        }
        return values
    class Meta:
        model = User
        fields = ('username', 'password', 'remember_me')
        widgets = {
            'password': forms.PasswordInput(),
        }    