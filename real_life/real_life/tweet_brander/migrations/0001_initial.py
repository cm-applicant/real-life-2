# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tweet'
        db.create_table(u'tweet_brander_tweet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('blocked', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'tweet_brander', ['Tweet'])


    def backwards(self, orm):
        # Deleting model 'Tweet'
        db.delete_table(u'tweet_brander_tweet')


    models = {
        u'tweet_brander.tweet': {
            'Meta': {'object_name': 'Tweet'},
            'blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['tweet_brander']