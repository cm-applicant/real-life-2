from django import forms
from django.forms import ModelForm
from django.conf import settings
from models import Tweet
import re

class TweetForm(ModelForm):
    
    def is_shameful(self):
        content = self.cleaned_data['content']
        
        for word, flag in settings.DIRTY_WORDS:
            if (flag and re.search(word, content, flag)) or re.search(word, content):
                return True
        
        return False
        
    def clean_content(self):
        content0 = content = self.cleaned_data['content']
        allrepl = 0
        
        for original, replacement, flags in settings.BRANDING:
            brandRE = re.compile(original, flags) if flags else re.compile(original)
            content, num = re.subn(brandRE, replacement, content)
            allrepl += num
        
        print original
        print content
        
        if allrepl > 0 and content0 != content:
            self.data['content'] = content
            raise forms.ValidationError('Your tweet has been rebranded!')
            
        return content
    
    class Meta:
        model = Tweet
        fields = ('content', 'owner', 'blocked', 'published',)
        widgets = {
            'content': forms.Textarea(attrs={'rows':2})
        }