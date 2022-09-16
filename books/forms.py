from dataclasses import field
from django import forms
from .models import BookUser

class userform(forms.ModelForm):
    class Meta:
        model = BookUser
        fields=['isbn','email_id','name']