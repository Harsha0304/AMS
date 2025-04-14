# inventory/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Asset, Vendor
from .forms import AssetForm, VendorForm
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'inventory/home.html')

@login_required
def asset_list(request):
    assets = Asset.objects.all()
    stats = {
        'total': assets.count(),
        'issued': assets.filter(status='issued').count(),
        'pending': assets.filter(status='pending').count(),
        'available': assets.filter(status='available').count(),
    }
    return render(request, 'inventory/asset_list.html', {'assets': assets, 'stats': stats})

@login_required
def asset_create(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new asset
            return redirect('asset_list')  # Redirect to asset list after save
    else:
        form = AssetForm()

    assets = Asset.objects.all()
    stats = {
        'total': assets.count(),
        'issued': assets.filter(status='issued').count(),
        'pending': assets.filter(status='pending').count(),
        'available': assets.filter(status='available').count(),
    }
    laptops = assets.filter(asset_type='laptop')

    return render(request, 'inventory/asset_form.html', {
        'form': form,
        'stats': stats,
        'laptops': laptops,
    })

@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'inventory/vendor_list.html', {'vendors': vendors})

@login_required
def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'inventory/vendor_form.html', {'form': form})
