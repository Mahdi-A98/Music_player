from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User
from django.utils.translation import gettext_lazy as _

import re

class UserRegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={'class': 'form-control'}), max_length=50)
    class Meta:
        model = User
        fields =  ["username","password","confirm_password", "first_name", "last_name", "email", "image"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'password': 'Password',
            'confirm_password': 'Password confirmation',
            'email': 'Email',
            'image': 'Image',
        }
        error_messages = {
            'username': {'required': 'This field is required',},
            'password': {'required': 'This field is required',},
            'confirm_password': {'required': 'This field is required',},
            }
        attrs = {
        'class' : {
            'username': 'form-control',
            'password': 'form-control',
        }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = None


    def clean_password(self):
        self.password = self.cleaned_data['password']
        pass_check = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[^A-Za-z0-9])(?=.{8,})')
        if not re.match(pass_check, self.password):
            raise forms.ValidationError('Password must has at least 8 character 1 digit and 1 special character!')
        return self.password

    def clean_confirm_password(self):
        password = self.password
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and (password !=confirm_password):
            raise ValidationError("Confirn password doesn't match")
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
