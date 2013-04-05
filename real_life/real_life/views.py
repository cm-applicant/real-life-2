from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
import twitter

def home(request):
    api = twitter.Api(consumer_key=settings.TW_C_KEY,
        consumer_secret=settings.TW_C_SECRET, 
        access_token_key=settings.TW_AT_KEY, 
        access_token_secret=settings.TW_AT_SECRET)
    
    tweets = api.GetUserTimeline('theCompanyAcct')
    
    return render_to_response('index.html', { 'tweets':tweets }, context_instance=RequestContext(request))