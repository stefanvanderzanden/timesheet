# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'TijdEntry.tijdsbesteding'
        db.delete_column(u'entries_tijdentry', 'tijdsbesteding')

        # Adding field 'TijdEntry.tijdbesteding'
        db.add_column(u'entries_tijdentry', 'tijdbesteding',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'TijdEntry.tijdsbesteding'
        db.add_column(u'entries_tijdentry', 'tijdsbesteding',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Deleting field 'TijdEntry.tijdbesteding'
        db.delete_column(u'entries_tijdentry', 'tijdbesteding')


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
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'verwachte_tijd': ('django.db.models.fields.FloatField', [], {})
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
            'tijdbesteding': ('django.db.models.fields.FloatField', [], {}),
            'titel': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['entries']