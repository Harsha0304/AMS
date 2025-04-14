from django.contrib import admin
from .models import Asset, Vendor, Employee, Laptop, Desktop, Server, VirtualMachine, Keyboard, Mouse, NetworkSwitch, Firewall, Router, SIMCard, Phone, Camera
from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Asset, Vendor
# Register your models here
# admin.site.register(Asset)
# admin.site.register(Vendor)
admin.site.register(Employee)
admin.site.register(Laptop)
admin.site.register(Desktop)
admin.site.register(Server)
admin.site.register(VirtualMachine)
admin.site.register(Keyboard)
admin.site.register(Mouse)
admin.site.register(NetworkSwitch)
admin.site.register(Firewall)
admin.site.register(Router)
admin.site.register(SIMCard)
admin.site.register(Phone)
admin.site.register(Camera)

@admin.register(Asset)
class AssetAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['name', 'serial_number', 'SIM_or_Dongle', 'vendor']

@admin.register(Vendor)
class VendorAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ['company_name', 'contact_person', 'phone_number']
