from django import forms
from .models import Asset, Vendor

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
