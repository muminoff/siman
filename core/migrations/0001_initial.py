# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CPUComponent'
        db.create_table('cpus', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
            ('cores', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'core', ['CPUComponent'])

        # Adding model 'CPUSize'
        db.create_table('cpu_sizes', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['CPUSize'])

        # Adding model 'StorageComponents'
        db.create_table('storages', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='HDD', max_length=3)),
            ('capacity', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'core', ['StorageComponents'])

        # Adding model 'StorageSize'
        db.create_table('storage_sizes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['StorageSize'])

        # Adding model 'GraphicCardComponent'
        db.create_table('graphic_cards', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['GraphicCardComponent'])

        # Adding model 'RAMComponent'
        db.create_table('rams', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['RAMComponent'])

        # Adding model 'RAMSize'
        db.create_table('ram_sizes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['RAMSize'])

        # Adding model 'ServerBay'
        db.create_table('bays', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['ServerBay'])

        # Adding model 'SelectableIPAddress'
        db.create_table('ip_addresses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['SelectableIPAddress'])

        # Adding model 'Customer'
        db.create_table('customers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Customer'])

        # Adding model 'SalesStaff'
        db.create_table('staff', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['SalesStaff'])

        # Adding model 'Server'
        db.create_table('servers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['Server'])


    def backwards(self, orm):
        # Deleting model 'CPUComponent'
        db.delete_table('cpus')

        # Deleting model 'CPUSize'
        db.delete_table('cpu_sizes')

        # Deleting model 'StorageComponents'
        db.delete_table('storages')

        # Deleting model 'StorageSize'
        db.delete_table('storage_sizes')

        # Deleting model 'GraphicCardComponent'
        db.delete_table('graphic_cards')

        # Deleting model 'RAMComponent'
        db.delete_table('rams')

        # Deleting model 'RAMSize'
        db.delete_table('ram_sizes')

        # Deleting model 'ServerBay'
        db.delete_table('bays')

        # Deleting model 'SelectableIPAddress'
        db.delete_table('ip_addresses')

        # Deleting model 'Customer'
        db.delete_table('customers')

        # Deleting model 'SalesStaff'
        db.delete_table('staff')

        # Deleting model 'Server'
        db.delete_table('servers')


    models = {
        u'core.cpucomponent': {
            'Meta': {'ordering': "['-cores', 'speed', 'name']", 'object_name': 'CPUComponent', 'db_table': "'cpus'"},
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