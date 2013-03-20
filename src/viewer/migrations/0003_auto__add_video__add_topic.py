# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Video'
        db.create_table(u'viewer_video', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dest_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nsfw', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posted_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('posted_channel', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('posted_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('video_id', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'viewer', ['Video'])

        # Adding model 'Topic'
        db.create_table(u'viewer_topic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nick', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('topic', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'viewer', ['Topic'])


    def backwards(self, orm):
        # Deleting model 'Video'
        db.delete_table(u'viewer_video')

        # Deleting model 'Topic'
        db.delete_table(u'viewer_topic')


    models = {
        u'viewer.image': {
            'Meta': {'object_name': 'Image'},
            'content_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dest_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'mirrored': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nsfw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted_channel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'viewer.link': {
            'Meta': {'object_name': 'Link'},
            'dest_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nsfw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted_channel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'viewer.topic': {
            'Meta': {'object_name': 'Topic'},
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'topic': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'viewer.video': {
            'Meta': {'object_name': 'Video'},
            'dest_url': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'nsfw': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted_channel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posted_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video_id': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['viewer']