# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Image'
        db.create_table(u'viewer_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dest_url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nsfw', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('posted_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('posted_channel', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('posted_by', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('mirrored', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'viewer', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Image'
        db.delete_table(u'viewer_image')


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
        }
    }

    complete_apps = ['viewer']