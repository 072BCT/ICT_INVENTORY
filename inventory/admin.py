from django.contrib import admin

# Register your models here.
from .models import Room, Computer, Printer, NetworkSwitch, AdditionalItem, RoomHasAdditionalItem, StoreItemName, \
    StoreItem, Laptop

admin.site.site_header = 'ICT Inventory, IOE'
admin.site.site_title = 'ICT Inventory'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'floor'
    )
    list_display = (
        'id',
        'floor'
    )
    search_fields = ('id',)
    list_filter = ('floor',)
    ordering = ('floor',)


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    fields = (
        'id',
        ('name', 'model'),
        'serial_no',
        'cost',
        'room',
        'date_of_acquire',
        'status'
    )
    list_display = (
        'id',
        'name',
        'model',
        'serial_no',
        'cost',
        'room',
        'date_of_acquire',
        'status',
        'created',
        'last_modified'
    )
    list_filter = (
        'status',
        'room',
        'date_of_acquire',
    )
    search_fields = (
        'id',
        'name',
        'model',
        'serial_no',
        'cost',
        'room__id',
        'date_of_acquire',
        'created',
        'last_modified'
    )


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    fields = (
        'id',
        ('name', 'model'),
        'serial_no',
        'cost',
        'date_of_acquire',
        'status'
    )
    list_display = (
        'id',
        'name',
        'model',
        'serial_no',
        'cost',
        'date_of_acquire',
        'status',
        'created',
        'last_modified'
    )
    list_filter = (
        'status',
        'date_of_acquire',
        'room__floor'
    )
    search_fields = (
        'id',
        'name',
        'model',
        'serial_no',
        'cost',
        'date_of_acquire',
        'created',
        'last_modified'
    )


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    fields = (
        'id',
        ('name', 'model'),
        'serial_no',
        'room',
        'cost',
        'date_of_acquire',
        'status'
    )
    list_display = (
        'id',
        'name',
        'model',
        'ip_address',
        'serial_no',
        'room',
        'cost',
        'date_of_acquire',
        'status',
        'created',
        'last_modified'
    )
    list_filter = (
        'status',
        'name',
        'room',
        'room__floor',
        'date_of_acquire',
    )
    search_fields = (
        'id',
        'name',
        'model',
        'serial_no',
        'ip_address',
        'room__id',
        'cost',
        'date_of_acquire',
        'created',
        'last_modified'
    )


@admin.register(NetworkSwitch)
class NetworkSwitchAdmin(admin.ModelAdmin):
    fields = (
        'id',
        ('name', 'model'),
        'serial_no',
        'no_of_ports',
        'no_of_SFP_ports',
        'room',
        'cost',
        'date_of_acquire',
        'status'
    )
    list_display = (
        'id',
        'name',
        'model',
        'serial_no',
        'room',
        'no_of_ports',
        'no_of_SFP_ports',
        'cost',
        'date_of_acquire',
        'status',
        'created',
        'last_modified'
    )
    list_filter = (
        'status',
        'name',
        'room',
        'date_of_acquire',
    )
    search_fields = (
        'id',
        'name',
        'model',
        'room__id',
        'cost',
        'date_of_acquire',
        'created',
        'last_modified'
    )


@admin.register(AdditionalItem)
class AdditionalItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    fields = (
        'id',
        'name'
    )
    search_fields = (
        'id',
        'name'
    )


@admin.register(RoomHasAdditionalItem)
class RoomHasAdditionalItemAdmin(admin.ModelAdmin):
    list_display = (
        'room',
        'additional_item',
        'quantity',
        'no_of_defect_items',
        'working_items',
        'last_modified'
    )
    fields = (
        'room',
        'additional_item',
        'quantity',
        'no_of_defect_items'
    )
    search_fields = (
        'room',
        'additional_item'
    )
    list_filter = (
        'room',
        'additional_item'
    )
    ordering = (
        'room',
        'additional_item'
    )

    def working_items(self, obj):
        return obj.quantity - obj.no_of_defect_items

    working_items.short_description = 'No of working items'


# @admin.register(StoreItemName)
# class StoreItemNameAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     fields = ('name',)
#     search_fields = ('name',)
#     ordering = ('name',)
#
#
# @admin.register(StoreItem)
# class StoreItemAdmin(admin.ModelAdmin):
#     list_display = (
#         'name',
#         'quantity',
#         'last_modified'
#     )
#     fields = (
#         'name',
#         'quantity'
#     )
#     search_fields = (
#         'name',
#     )
#     ordering = (
#         'name',
#     )
