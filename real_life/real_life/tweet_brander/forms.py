from django import forms
from django.forms import ModelForm
from django.conf import settings
from models import Tweet
import re

class TweetForm(ModelForm):
    
    def clean_content(self):
        content = self.cleaned_data['content']
        
        for word, flag in settings.DIRTY_WORDS:
            if (flag and re.search(word, content, flag)) or re.search(word, content):
                print 'regex that failed validation: %s' % word
                raise forms.ValidationError('Shame on you!')
        
        return content
    
    class Meta:
        model = Tweet
        fields = ('content', 'owner', 'blocked', 'published',)
        widgets = {
            'content': forms.Textarea(attrs={'rows':2})
        }