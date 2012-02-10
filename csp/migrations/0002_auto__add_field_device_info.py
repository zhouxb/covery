# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Device.info'
        db.add_column('csp_device', 'info', self.gf('django.db.models.fields.CharField')(default='sdfa', max_length=1000), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Device.info'
        db.delete_column('csp_device', 'info')


    models = {
        'csp.device': {
            'Meta': {'object_name': 'Device'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'external_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
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
