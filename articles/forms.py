from django import forms
from .models import Article




class AritcleForm(forms.ModelForm):
    class Meta():
        model = Article
        exclude = ('user',)