# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Device'
        db.create_table('csp_device', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('intranet_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('external_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('sn', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('os', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('safe', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('remark', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('csp', ['Device'])


    def backwards(self, orm):
        
        # Deleting model 'Device'
        db.delete_table('csp_device')


    models = {
        'csp.device': {
            'Meta': {'object_name': 'Device'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'external_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intranet_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'os': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'remark': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'safe': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sn': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['csp']
