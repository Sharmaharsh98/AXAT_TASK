from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'name', 'contact_number', 'role', 'is_staff', 'is_active']

        ROLES = (
        ('----', '-----'),
        ('TEACHER', 'TEACHER'),
        ('STUDENT', 'STUDENT')
    )

        widgets = {
            'email' : forms.EmailInput(),
            'name' : forms.TextInput(),
            'role' : forms.Select(choices=ROLES)
        }

class UserForm1(UserChangeForm):

    class Meta:
        model = User
        fields = ['email', 'name', 'contact_number', 'role', 'is_staff', 'is_active']