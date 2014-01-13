from django.contrib import admin
from core.models import Serial, MainboardComponent, CPUComponent, CPUSize, StorageComponent, StorageSize, MemoryComponent, MemorySize, ServerBay, SelectableIPAddress, Customer, SalesStaff, Server


class SerialAdmin(admin.ModelAdmin):
    exclude = ('id',)

admin.site.register(Serial, SerialAdmin)
admin.site.register(MainboardComponent)
admin.site.register(CPUComponent)
admin.site.register(CPUSize)
admin.site.register(StorageComponent)
admin.site.register(StorageSize)
admin.site.register(MemoryComponent)
admin.site.register(MemorySize)
admin.site.register(ServerBay)
admin.site.register(SelectableIPAddress)
admin.site.register(Customer)
admin.site.register(SalesStaff)
admin.site.register(Server)
