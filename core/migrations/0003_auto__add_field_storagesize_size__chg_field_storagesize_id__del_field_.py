# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'StorageSize.size'
        db.add_column('storage_sizes', 'size',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


        # Changing field 'StorageSize.id'
        db.alter_column('storage_sizes', 'id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True))
        # Deleting field 'CPUComponent.vendor'
        db.delete_column('cpus', 'vendor')

        # Deleting field 'CPUComponent.brand'
        db.delete_column('cpus', 'brand')

        # Deleting field 'CPUComponent.slug'
        db.delete_column('cpus', 'slug')

        # Adding field 'CPUComponent.manufacturer'
        db.add_column('cpus', 'manufacturer',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CPUComponent.model_number'
        db.add_column('cpus', 'model_number',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CPUComponent.socket'
        db.add_column('cpus', 'socket',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'StorageSize.size'
        db.delete_column('storage_sizes', 'size')


        # Changing field 'StorageSize.id'
        db.alter_column('storage_sizes', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Adding field 'CPUComponent.vendor'
        db.add_column('cpus', 'vendor',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'CPUComponent.brand'
        db.add_column('cpus', 'brand',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'CPUComponent.slug'
        raise RuntimeError("Cannot reverse this migration. 'CPUComponent.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'CPUComponent.slug'
        db.add_column('cpus', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50),
                      keep_default=False)

        # Deleting field 'CPUComponent.manufacturer'
        db.delete_column('cpus', 'manufacturer')

        # Deleting field 'CPUComponent.model_number'
        db.delete_column('cpus', 'model_number')

        # Deleting field 'CPUComponent.socket'
        db.delete_column('cpus', 'socket')


    models = {
        u'core.cpucomponent': {
            'Meta': {'ordering': "['-cores', 'speed', 'name']", 'object_name': 'CPUComponent', 'db_table': "'cpus'"},
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
            'id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'primary_key': 'True'}),
            'size': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['core']