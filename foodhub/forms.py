from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ChefRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    bio = forms.CharField(widget=forms.Textarea, required=True)
    photo = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'photo']