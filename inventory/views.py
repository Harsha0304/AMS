from django.shortcuts import render, redirect, get_object_or_404
from .models import Asset, Vendor
from .forms import AssetForm, VendorForm

def home(request):
    return render(request, 'inventory/home.html')

def asset_list(request):
    assets = Asset.objects.all()
    return render(request, 'inventory/asset_list.html', {'assets': assets})

def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'inventory/asset_form.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'inventory/vendor_list.html', {'vendors': vendors})

def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'inventory/vendor_form.html', {'form': form})
