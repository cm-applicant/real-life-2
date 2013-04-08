from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from django.db.models import Q
from django.core.urlresolvers import reverse
import twitter
from models import Tweet
from forms import TweetForm
from datetime import datetime

def home(request):
    api = twitter.Api(consumer_key=settings.TW_C_KEY,
        consumer_secret=settings.TW_C_SECRET, 
        access_token_key=settings.TW_AT_KEY, 
        access_token_secret=settings.TW_AT_SECRET)
    
    is_sub = request.user.has_perm('tweet_brander.submit_tweet')
    is_mod = request.user.has_perm('tweet_brander.moderate_tweet')
    is_pub = request.user.has_perm('tweet_brander.publish_tweet')
    
    tweet_filter = Q(content__exact='')
    if is_sub:
        tweet_filter |= Q(owner=request.user)
    if is_mod:
        tweet_filter |= Q(published=False) | Q(blocked=True)
    if is_pub:
        tweet_filter |= Q(published=False)
    
    tpl_data = {
        'tweets': api.GetUserTimeline('theCompanyAcct'),
        'pretweets': Tweet.objects.filter(tweet_filter).order_by('-pub_date')
    }

    return render_to_response('tweet_brander/index.html', tpl_data, 
        context_instance=RequestContext(request))
    
def submit(request):
    if request.method == 'GET':
        form = TweetForm({'owner': request.user}, auto_id=True)
    else:
        form = TweetForm(request.POST, auto_id=True)
        if form.is_valid():
            form.instance.pub_date = datetime.now()
            form.instance.save()
            
            return HttpResponseRedirect(reverse('home'))
        
    tpl_data = {
        'form': form
    }
    
    return render_to_response('tweet_brander/submit.html', tpl_data,
        context_instance=RequestContext(request))
        
def moderate(request, id):
    tweet = Tweet.objects.get(id=id)
    form = TweetForm(instance=tweet)
    
    tpl_data = {
        'form': form
    }
    
    return render_to_response('tweet_brander/moderate.html', tpl_data,
        context_instance=RequestContext(request))