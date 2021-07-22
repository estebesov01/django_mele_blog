from django import forms
from .models import Comment, EmailPost


class EmailPostForm(forms.ModelForm):
    class Meta:
        model = EmailPost
        fields = ('name', 'to', 'comments')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
