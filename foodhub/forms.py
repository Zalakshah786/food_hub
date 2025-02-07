from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Chef_Comment
from .models import CollaborateRequest



class ChefCommentForm(forms.ModelForm):
    class Meta:
        model = Chef_Comment
        fields = ['text', 'rating']

class CollaborateRequestForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ['name', 'email', 'message']
       
