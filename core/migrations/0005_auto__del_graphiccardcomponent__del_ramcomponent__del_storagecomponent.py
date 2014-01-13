# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'GraphicCardComponent'
        db.delete_table('graphic_cards')

        # Deleting model 'RAMComponent'
        db.delete_table('rams')

        # Deleting model 'StorageComponents'
        db.delete_table('storages')

        # Deleting model 'RAMSize'
        db.delete_table('ram_sizes')

        # Adding model 'Serial'
        db.create_table(u'core_serial', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'core', ['Serial'])

        # Adding model 'MemoryComponent'
        db.create_table('memories', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('speed', self.gf('django.db.models.fields.FloatField')()),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
        ))
        db.send_create_signal(u'core', ['MemoryComponent'])

        # Adding model 'StorageComponent'
        db.create_table('storages', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='HDD', max_length=3)),
            ('capacity', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'core', ['StorageComponent'])

        # Adding model 'MemorySize'
        db.create_table('memory_sizes', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
            ('size', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['MemorySize'])

        # Adding field 'Customer.name'
        db.add_column('customers', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=20),
                      keep_default=False)


        # Changing field 'Customer.id'
        db.alter_column('customers', 'id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True))
        # Adding field 'SalesStaff.name'
        db.add_column('staff', 'name',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=20),
                      keep_default=False)


        # Changing field 'SalesStaff.id'
        db.alter_column('staff', 'id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True))
        # Adding field 'SelectableIPAddress.address'
        db.add_column('ip_addresses', 'address',
                      self.gf('django.db.models.fields.IPAddressField')(default='', max_length=15),
                      keep_default=False)


        # Changing field 'SelectableIPAddress.id'
        db.alter_column('ip_addresses', 'id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True))
        # Adding field 'ServerBay.size'
        db.add_column('bays', 'size',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


        # Changing field 'ServerBay.id'
        db.alter_column('bays', 'id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True))
        # Adding field 'Server.assembled'
        db.add_column('servers', 'assembled',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 1, 9, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)

        # Adding field 'Server.updated'
        db.add_column('servers', 'updated',
                      self.gf('django.db.models.fields.DateField')(auto_now=True, default=datetime.datetime(2014, 1, 9, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Server.serial'
        db.add_column('servers', 'serial',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['core.Serial'], unique=True),
                      keep_default=False)

        # Adding field 'Server.cpu'
        db.add_column('servers', 'cpu',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['core.CPUComponent']),
                      keep_default=False)

        # Adding field 'Server.cpu_limit'
        db.add_column('servers', 'cpu_limit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.CPUSize']),
                      keep_default=False)

        # Adding field 'Server.storage_limit'
        db.add_column('servers', 'storage_limit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['core.StorageSize']),
                      keep_default=False)

        # Adding field 'Server.memory_limit'
        db.add_column('servers', 'memory_limit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['core.MemorySize']),
                      keep_default=False)

        # Adding field 'Server.bay'
        db.add_column('servers', 'bay',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['core.ServerBay']),
                      keep_default=False)

        # Adding field 'Server.customer'
        db.add_column('servers', 'customer',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['core.Customer']),
                      keep_default=False)

        # Adding field 'Server.responsible_person'
        db.add_column('servers', 'responsible_person',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['core.SalesStaff']),
                      keep_default=False)

        # Adding field 'Server.notes'
        db.add_column('servers', 'notes',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Adding M2M table for field storage on 'Server'
        m2m_table_name = db.shorten_name('servers_storage')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('server', models.ForeignKey(orm[u'core.server'], null=False)),
            ('storagecomponent', models.ForeignKey(orm[u'core.storagecomponent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['server_id', 'storagecomponent_id'])

        # Adding M2M table for field memories on 'Server'
        m2m_table_name = db.shorten_name('servers_memories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('server', models.ForeignKey(orm[u'core.server'], null=False)),
            ('memorycomponent', models.ForeignKey(orm[u'core.memorycomponent'], null=False))
        ))
        db.create_unique(m2m_table_name, ['server_id', 'memorycomponent_id'])

        # Adding M2M table for field ip_address on 'Server'
        m2m_table_name = db.shorten_name('servers_ip_address')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('server', models.ForeignKey(orm[u'core.server'], null=False)),
            ('selectableipaddress', models.ForeignKey(orm[u'core.selectableipaddress'], null=False))
        ))
        db.create_unique(m2m_table_name, ['server_id', 'selectableipaddress_id'])


    def backwards(self, orm):
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

        # Adding model 'StorageComponents'
        db.create_table('storages', (
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True)),
            ('capacity', self.gf('django.db.models.fields.BigIntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='HDD', max_length=3)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=16, primary_key=True)),
        ))
        db.send_create_signal(u'core', ['StorageComponents'])

        # Adding model 'RAMSize'
        db.create_table('ram_sizes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'core', ['RAMSize'])

        # Deleting model 'Serial'
        db.delete_table(u'core_serial')

        # Deleting model 'MemoryComponent'
        db.delete_table('memories')

        # Deleting model 'StorageComponent'
        db.delete_table('storages')

        # Deleting model 'MemorySize'
        db.delete_table('memory_sizes')

        # Deleting field 'Customer.name'
        db.delete_column('customers', 'name')


        # Changing field 'Customer.id'
        db.alter_column('customers', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Deleting field 'SalesStaff.name'
        db.delete_column('staff', 'name')


        # Changing field 'SalesStaff.id'
        db.alter_column('staff', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Deleting field 'SelectableIPAddress.address'
        db.delete_column('ip_addresses', 'address')


        # Changing field 'SelectableIPAddress.id'
        db.alter_column('ip_addresses', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Deleting field 'ServerBay.size'
        db.delete_column('bays', 'size')


        # Changing field 'ServerBay.id'
        db.alter_column('bays', u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))
        # Deleting field 'Server.assembled'
        db.delete_column('servers', 'assembled')

        # Deleting field 'Server.updated'
        db.delete_column('servers', 'updated')

        # Deleting field 'Server.serial'
        db.delete_column('servers', 'serial_id')

        # Deleting field 'Server.cpu'
        db.delete_column('servers', 'cpu_id')

        # Deleting field 'Server.cpu_limit'
        db.delete_column('servers', 'cpu_limit_id')

        # Deleting field 'Server.storage_limit'
        db.delete_column('servers', 'storage_limit_id')

        # Deleting field 'Server.memory_limit'
        db.delete_column('servers', 'memory_limit_id')

        # Deleting field 'Server.bay'
        db.delete_column('servers', 'bay_id')

        # Deleting field 'Server.customer'
        db.delete_column('servers', 'customer_id')

        # Deleting field 'Server.responsible_person'
        db.delete_column('servers', 'responsible_person_id')

        # Deleting field 'Server.notes'
        db.delete_column('servers', 'notes')

        # Removing M2M table for field storage on 'Server'
        db.delete_table(db.shorten_name('servers_storage'))

        # Removing M2M table for field memories on 'Server'
        db.delete_table(db.shorten_name('servers_memories'))

        # Removing M2M table for field ip_address on 'Server'
        db.delete_table(db.shorten_name('servers_ip_address'))


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
