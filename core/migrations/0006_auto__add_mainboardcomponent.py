# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MainboardComponent'
        db.create_table('mainboards', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('model_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('socket', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('architecture', self.gf('django.db.models.fields.CharField')(default='64-bit', max_length=8)),
        ))
        db.send_create_signal(u'core', ['MainboardComponent'])


    def backwards(self, orm):
        # Deleting model 'MainboardComponent'
        db.delete_table('mainboards')


    models = {
        u'core.cpucomponent': {
            'Meta': {'ordering': "['-cores', 'speed', 'name']", 'object_name': 'CPUComponent', 'db_table': "'cpus'"},
            'architecture': ('django.db.models.fields.CharField', [], {'default': "'64-bit'", 'max_length': '8'}),
            'cores': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'model_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'socket': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        u'core.cpusize': {
            'Meta': {'ordering': "['size']", 'object_name': 'CPUSize', 'db_table': "'cpu_sizes'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "'customers'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'core.mainboardcomponent': {
            'Meta': {'ordering': "['name', 'manufacturer']", 'object_name': 'MainboardComponent', 'db_table': "'mainboards'"},
            'architecture': ('django.db.models.fields.CharField', [], {'default': "'64-bit'", 'max_length': '8'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'model_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'socket': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'core.memorycomponent': {
            'Meta': {'ordering': "['-size', 'name']", 'object_name': 'MemoryComponent', 'db_table': "'memories'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'speed': ('django.db.models.fields.FloatField', [], {})
        },
        u'core.memorysize': {
            'Meta': {'ordering': "['size']", 'object_name': 'MemorySize', 'db_table': "'memory_sizes'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.salesstaff': {
            'Meta': {'object_name': 'SalesStaff', 'db_table': "'staff'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'core.selectableipaddress': {
            'Meta': {'object_name': 'SelectableIPAddress', 'db_table': "'ip_addresses'"},
            'address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'})
        },
        u'core.serial': {
            'Meta': {'object_name': 'Serial'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'core.server': {
            'Meta': {'object_name': 'Server', 'db_table': "'servers'"},
            'assembled': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 1, 9, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
            'bay': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.ServerBay']"}),
            'cpu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CPUComponent']"}),
            'cpu_limit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.CPUSize']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Customer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.SelectableIPAddress']", 'symmetrical': 'False'}),
            'memories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.MemoryComponent']", 'symmetrical': 'False'}),
            'memory_limit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.MemorySize']"}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'responsible_person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.SalesStaff']"}),
            'serial': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Serial']", 'unique': 'True'}),
            'storage': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.StorageComponent']", 'symmetrical': 'False'}),
            'storage_limit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.StorageSize']"}),
            'updated': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'core.serverbay': {
            'Meta': {'object_name': 'ServerBay', 'db_table': "'bays'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.storagecomponent': {
            'Meta': {'ordering': "['capacity']", 'object_name': 'StorageComponent', 'db_table': "'storages'"},
            'capacity': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'HDD'", 'max_length': '3'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'core.storagesize': {
            'Meta': {'object_name': 'StorageSize', 'db_table': "'storage_sizes'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['core']