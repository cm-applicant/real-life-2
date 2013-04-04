from django.db import models

class Tweet (models.Model):
    content = models.CharField(max_length=140)
    blocked = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    pub_date = models.DateTimeField()