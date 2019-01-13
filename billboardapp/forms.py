from django import forms
from .models import Posts, Comments
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Author'}),label='')
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title'}),label='')
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter post here'}), label='')

    class Meta:
        model = Posts
        fields = ('title', 'text', 'author')


class CommentForm(forms.ModelForm):
    
    text_comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter comment here'}), label='')

    class Meta:
        model = Comments
        fields = ['text_comment']

