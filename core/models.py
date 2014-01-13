from django.db import models
from uuid import uuid4
from datetime import date
from django.utils.translation import ugettext as _


class Serial(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    serial = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(Serial, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.serial


class MainboardComponent(models.Model):
    ARCH32 = _('32-bit')
    ARCH64 = _('64-bit')
    ARCHITECTURE = ((ARCH32, _('32-bit')),(ARCH64, _('64-bit')))
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    manufacturer = models.CharField(max_length=20, null=True, blank=True)
    model_number = models.CharField(max_length=20, null=True, blank=True)
    socket = models.CharField(max_length=10, null=True, blank=True)
    architecture = models.CharField(max_length=8, choices=ARCHITECTURE, default=ARCH64)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(MainboardComponent, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s %s".format(self.name, self.manufacturer)

    class Meta:
        db_table = "mainboards"
        ordering = ['name', 'manufacturer',]
    

class CPUComponent(models.Model):
    ARCH32 = _('32-bit')
    ARCH64 = _('64-bit')
    ARCHITECTURE = ((ARCH32, _('32-bit')),(ARCH64, _('64-bit')))
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    manufacturer = models.CharField(max_length=20, null=True, blank=True)
    model_number = models.CharField(max_length=20, null=True, blank=True)
    socket = models.CharField(max_length=10, null=True, blank=True)
    speed = models.FloatField()
    cores = models.PositiveIntegerField()
    architecture = models.CharField(max_length=8, choices=ARCHITECTURE, default=ARCH64)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(CPUComponent, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s %s".format(self.name, self.manufacturer)

    class Meta:
        db_table = "cpus"
        ordering = ['-cores', 'speed', 'name',]
    

class CPUSize(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    size = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(CPUSize, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.size)

    class Meta:
        db_table = "cpu_sizes"
        ordering = ['size',]


class StorageComponent(models.Model):
    HDD = 'HDD'
    SSD = 'SSD'
    DISK_TYPES = ((HDD, _('Hard Disk Drive')),(SSD, 'Solid State Disk'))
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    vendor = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=3, choices=DISK_TYPES, default=HDD)
    capacity = models.BigIntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(StorageComponent, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s %s".format(self.name, self.vendor)

    class Meta:
        db_table = "storages"
        ordering = ['capacity',]


class StorageSize(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    size = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(StorageSize, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.size)

    class Meta:
        db_table = "storage_sizes"


class MemoryComponent(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    speed = models.FloatField()
    size = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(MemoryComponent, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s %s".format(self.name, self.vendor)

    class Meta:
        db_table = "memories"
        ordering = ['-size', 'name',]


class MemorySize(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    size = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(MemorySize, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.size)

    class Meta:
        db_table = "memory_sizes"
        ordering = ['size',]



class ServerBay(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    size = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(ServerBay, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.size)

    class Meta:
        db_table = "bays"


class SelectableIPAddress(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    address = models.IPAddressField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(SelectableIPAddress, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.address)

    class Meta:
        db_table = "ip_addresses"


class Customer(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(Customer, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.name)


    class Meta:
        db_table = "customers"


class SalesStaff(models.Model):
    id = models.CharField(max_length=16, primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(uuid4()).replace('-','')[:16]

        super(SalesStaff, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"%s".format(self.name)


    class Meta:
        db_table = "staff"


class Server(models.Model):
    assembled = models.DateField(auto_now_add=True, default=date.today())
    updated = models.DateField(auto_now=True)
    serial = models.ForeignKey(Serial, unique=True)
    cpu = models.ForeignKey(CPUComponent)
    cpu_limit = models.ForeignKey(CPUSize)
    storage = models.ManyToManyField(StorageComponent)
    storage_limit = models.ForeignKey(StorageSize)
    memories = models.ManyToManyField(MemoryComponent)
    memory_limit = models.ForeignKey(MemorySize)
    bay = models.ForeignKey(ServerBay)
    ip_address = models.ManyToManyField(SelectableIPAddress)
    customer = models.ForeignKey(Customer)
    responsible_person = models.ForeignKey(SalesStaff)
    notes = models.TextField()


    class Meta:
        db_table = "servers"
