# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CPUComponent.brand'
        db.add_column('cpus', 'brand',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CPUComponent.brand'
        db.delete_column('cpus', 'brand')


    models = {
        u'core.cpucomponent': {
            'Meta': {'ordering': "['-cores', 'speed', 'name']", 'object_name': 'CPUComponent', 'db_table': "'cpus'"},
            'brand': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cores': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'speed': ('django.db.models.fields.FloatField', [], {}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'core.cpusize': {
            'Meta': {'ordering': "['size']", 'object_name': 'CPUSize', 'db_table': "'cpu_sizes'"},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'core.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "'customers'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.graphiccardcomponent': {
            'Meta': {'object_name': 'GraphicCardComponent', 'db_table': "'graphic_cards'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.ramcomponent': {
            'Meta': {'object_name': 'RAMComponent', 'db_table': "'rams'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.ramsize': {
            'Meta': {'object_name': 'RAMSize', 'db_table': "'ram_sizes'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.salesstaff': {
            'Meta': {'object_name': 'SalesStaff', 'db_table': "'staff'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.selectableipaddress': {
            'Meta': {'object_name': 'SelectableIPAddress', 'db_table': "'ip_addresses'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.server': {
            'Meta': {'object_name': 'Server', 'db_table': "'servers'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.serverbay': {
            'Meta': {'object_name': 'ServerBay', 'db_table': "'bays'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.storagecomponents': {
            'Meta': {'ordering': "['capacity']", 'object_name': 'StorageComponents', 'db_table': "'storages'"},
            'capacity': ('django.db.models.fields.BigIntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'HDD'", 'max_length': '3'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'core.storagesize': {
            'Meta': {'object_name': 'StorageSize', 'db_table': "'storage_sizes'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']