from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Tweet (models.Model):
    content = models.CharField(max_length=140)
    blocked = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
class Tweeter (AbstractUser):
    
    class Meta:
        permissions = (
            ('submit_tweet', 'Can submit a tweet.'),
            ('moderate_tweet', 'Can moderate a tweet.'),
            ('publish_tweet', 'Can publish a tweet.'),
        )