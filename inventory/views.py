# inventory/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Asset, Vendor
from .forms import AssetForm, VendorForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Asset, Vendor, Employee
from .forms import AssetForm, VendorForm, EmployeeForm

# User Login view
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

# User Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Home view - after login
@login_required
def home(request):
    return render(request, 'inventory/home.html')

# Asset List view - lists all assets with stats
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

# Asset Create view - form to create a new asset
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

# Vendor List view - lists all vendors
@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'inventory/vendor_list.html', {'vendors': vendors})

# Vendor Create view - form to create a new vendor
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

# Employee List view - lists all employees
@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'inventory/employee_list.html', {'employees': employees})

# Employee Create view - form to create a new employee
@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'inventory/employee_form.html', {'form': form})

# Employee Detail view - shows details of a single employee including assigned assets
@login_required
def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    assets = Asset.objects.filter(assigned_to=employee.name)
    return render(request, 'inventory/employee_detail.html', {'employee': employee, 'assets': assets})

# Asset Detail view - shows detailed information about an asset
@login_required
def asset_detail(request, asset_id):
    asset = Asset.objects.get(id=asset_id)
    return render(request, 'inventory/asset_detail.html', {'asset': asset})
