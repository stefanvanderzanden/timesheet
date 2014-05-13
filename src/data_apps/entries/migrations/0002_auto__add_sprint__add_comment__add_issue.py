# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sprint'
        db.create_table(u'entries_sprint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('deadline', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'entries', ['Sprint'])

        # Adding model 'Comment'
        db.create_table(u'entries_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('sprint', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comment_sprint', to=orm['entries.Sprint'])),
        ))
        db.send_create_signal(u'entries', ['Comment'])

        # Adding model 'Issue'
        db.create_table(u'entries_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sprint', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issue_sprint', to=orm['entries.Sprint'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('urgency', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submitter', to=orm['auth.User'])),
            ('assignee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assignee', to=orm['auth.User'])),
            ('estimated_time', self.gf('django.db.models.fields.IntegerField')()),
            ('spend_time', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'entries', ['Issue'])


    def backwards(self, orm):
        # Deleting model 'Sprint'
        db.delete_table(u'entries_sprint')

        # Deleting model 'Comment'
        db.delete_table(u'entries_comment')

        # Deleting model 'Issue'
        db.delete_table(u'entries_issue')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'entries.comment': {
            'Meta': {'object_name': 'Comment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_sprint'", 'to': u"orm['entries.Sprint']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'entries.issue': {
            'Meta': {'object_name': 'Issue'},
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'assignee'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'estimated_time': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'spend_time': ('django.db.models.fields.IntegerField', [], {}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'issue_sprint'", 'to': u"orm['entries.Sprint']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'submitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submitter'", 'to': u"orm['auth.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'urgency': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'entries.sprint': {
            'Meta': {'object_name': 'Sprint'},
            'deadline': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['entries']