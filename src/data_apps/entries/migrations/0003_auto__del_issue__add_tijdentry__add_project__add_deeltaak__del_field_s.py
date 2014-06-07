# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Issue'
        db.delete_table(u'entries_issue')

        # Adding model 'TijdEntry'
        db.create_table(u'entries_tijdentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
            ('tijdsbesteding', self.gf('django.db.models.fields.FloatField')()),
            ('deeltaak', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tijdentry_deeltaak', to=orm['entries.DeelTaak'])),
        ))
        db.send_create_signal(u'entries', ['TijdEntry'])

        # Adding model 'Project'
        db.create_table(u'entries_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
            ('deadline', self.gf('django.db.models.fields.DateField')()),
            ('sprint', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project_sprint', to=orm['entries.Sprint'])),
        ))
        db.send_create_signal(u'entries', ['Project'])

        # Adding model 'DeelTaak'
        db.create_table(u'entries_deeltaak', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titel', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('beschrijving', self.gf('django.db.models.fields.TextField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='deeltaak_project', to=orm['entries.Project'])),
        ))
        db.send_create_signal(u'entries', ['DeelTaak'])

        # Deleting field 'Sprint.title'
        db.delete_column(u'entries_sprint', 'title')

        # Deleting field 'Sprint.deadline'
        db.delete_column(u'entries_sprint', 'deadline')

        # Deleting field 'Sprint.description'
        db.delete_column(u'entries_sprint', 'description')

        # Adding field 'Sprint.titel'
        db.add_column(u'entries_sprint', 'titel',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Comment.datetime'
        db.add_column(u'entries_comment', 'datetime',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=None, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Issue'
        db.create_table(u'entries_issue', (
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('spend_time', self.gf('django.db.models.fields.IntegerField')()),
            ('estimated_time', self.gf('django.db.models.fields.IntegerField')()),
            ('assignee', self.gf('django.db.models.fields.related.ForeignKey')(related_name='assignee', to=orm['auth.User'])),
            ('sprint', self.gf('django.db.models.fields.related.ForeignKey')(related_name='issue_sprint', to=orm['entries.Sprint'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('submitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='submitter', to=orm['auth.User'])),
            ('urgency', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'entries', ['Issue'])

        # Deleting model 'TijdEntry'
        db.delete_table(u'entries_tijdentry')

        # Deleting model 'Project'
        db.delete_table(u'entries_project')

        # Deleting model 'DeelTaak'
        db.delete_table(u'entries_deeltaak')

        # Adding field 'Sprint.title'
        db.add_column(u'entries_sprint', 'title',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=50),
                      keep_default=False)

        # Adding field 'Sprint.deadline'
        db.add_column(u'entries_sprint', 'deadline',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)

        # Adding field 'Sprint.description'
        db.add_column(u'entries_sprint', 'description',
                      self.gf('django.db.models.fields.TextField')(default=None),
                      keep_default=False)

        # Deleting field 'Sprint.titel'
        db.delete_column(u'entries_sprint', 'titel')

        # Deleting field 'Comment.datetime'
        db.delete_column(u'entries_comment', 'datetime')


    models = {
        u'entries.comment': {
            'Meta': {'object_name': 'Comment'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comment_sprint'", 'to': u"orm['entries.Sprint']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'entries.deeltaak': {
            'Meta': {'object_name': 'DeelTaak'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deeltaak_project'", 'to': u"orm['entries.Project']"}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'entries.project': {
            'Meta': {'object_name': 'Project'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'deadline': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_sprint'", 'to': u"orm['entries.Sprint']"}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'entries.sprint': {
            'Meta': {'object_name': 'Sprint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'entries.tijdentry': {
            'Meta': {'object_name': 'TijdEntry'},
            'beschrijving': ('django.db.models.fields.TextField', [], {}),
            'deeltaak': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tijdentry_deeltaak'", 'to': u"orm['entries.DeelTaak']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tijdsbesteding': ('django.db.models.fields.FloatField', [], {}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['entries']