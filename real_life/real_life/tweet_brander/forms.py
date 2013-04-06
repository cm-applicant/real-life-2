from django import forms
from django.forms import ModelForm
from models import Tweet

class TweetForm(ModelForm):
            
    def clean_owner(self):
        return self.instance.owner
        
    class Meta:
        model = Tweet
        fields = ('content', 'owner', 'blocked', 'published',)
        widgets = {
            'content': forms.Textarea(attrs={'rows':2})
        }