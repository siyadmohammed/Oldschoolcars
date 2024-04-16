from django.contrib.auth.forms import UserCreationForm

from store.models import User

from django import forms

class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-box my-2', 'placeholder': 'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input-box my-2', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box my-2', 'placeholder': 'Enter '
                                                                                                            'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-box my-2', 'placeholder': 'Confirm '
                                                                                                            'password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
