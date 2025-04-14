# inventory/forms.py
from django import forms
from .models import Asset, Vendor, Employee  # Assuming Employee model exists

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'serial_number', 'assigned_to', 'purchase_date', 'vendor', 'asset_type', 'status', 'SIM_or_Dongle', 'dongle_type', 'dongle_id', 'sim_name', 'sim_phone_number', 'sim_ccid_number']
        widgets = {
            'asset_type': forms.Select(choices=Asset.ASSET_TYPE_CHOICES),
            'status': forms.Select(choices=Asset.STATUS_CHOICES),
        }

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'contact', 'address']  # Adjust fields as per your model
        

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee  # Assuming you have an Employee model
        fields = ['name', 'email', 'phone', 'department']  # Adjust fields as per your model
