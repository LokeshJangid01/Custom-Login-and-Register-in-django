from distutils.log import error
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#user registeration part

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "placeholder":'Username',
            'class':'form-control'
        }
    ),error_messages={
        'required':'The username field is required'
        
    })
    
    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs={
                'palceholder':'Email',
                'class':'form-control'
            }
            
        ),error_messages={
            'required':'The email is requirement'
            
        })
    
    password1 = forms.CharField(
    widget=forms.PasswordInput(
        attrs={
            "placeholder": "Password",
            "class": "form-control"
        }
    ),error_messages={
               'required': 'The password field is required.'
    })
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(
        attrs={
            "placeholder": "Conform Password",
            "class": "form-control"
        }
    ),error_messages={
               'required': 'The Conform password field is required.'
    })
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        
    
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                 "placeholder": "Username",
                 "class": "form-control"
        }
    ),error_messages={
            'required': 'The username field is required.'
    })
    password = forms.CharField(
        widget=forms.PasswordInput(
              attrs={
                 "placeholder": "Password",
                 "class": "form-control"
        }
    ),error_messages={
            'required': 'The password field is required.'
    })