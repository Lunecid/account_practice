from django import forms
from .models import Article, Comment




class AritcleForm(forms.ModelForm):
    class Meta():
        model = Article
        exclude = ('user',)


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('content',)