from django import forms
from django.forms import ModelForm
from models import Tweet

class TweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ('content', 'owner', 'blocked', 'published',)
        widgets = {
            'content': forms.Textarea(attrs={'rows':2})
        }